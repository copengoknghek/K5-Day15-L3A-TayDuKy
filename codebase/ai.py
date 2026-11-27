"""Nối model — chỗ DUY NHẤT trong bản chạy thử gọi model AI. NHÓM VIẾT phần gọi model thật.

Hợp đồng (giữ nguyên để khung đo được token):
    call_model(system: str, user: str) -> dict với 4 khoá
        "text":       str   chữ model trả về
        "model":      str   tên model đã gọi (để tra giá ở bảng giá model)
        "tokens_in":  int   số token vào, lấy từ trường usage trong phản hồi API — KHÔNG ước lượng
        "tokens_out": int   số token ra, gồm cả token suy luận / suy nghĩ nếu API tính riêng
    @model_call (từ tracing.py) tự ghi mỗi lần gọi vào trace; agent.py gọi call_model bao nhiêu lần
    cũng được, khung tự cộng token.
    Lỗi gọi model (hết lượt, sai key, mất mạng): cứ để exception bay ra — khung ghi lỗi vào cột error.

Chế độ giả (mặc định khi .env chưa có MODEL_PROVIDER, hoặc MODEL_PROVIDER=fake):
    trả một câu giả cố định, model "fake", token 0 — để luồng chạy hết từ trước CP2 (guide bước 3.2).
    Lượt `run.py eval` / `run.py simulate` chạy bằng model giả KHÔNG được tính.

Nối model thật: điền .env (chép từ .env.example), không cần sửa file này. Đã có: gemini · openai ·
anthropic · ollama (theo docs/connect-model.md; gemini dùng API dạng OpenAI của Google).
Không dán API key vào file này.
"""
import json
import os
import urllib.error
import urllib.request

from tracing import model_call

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env(path=os.path.join(ROOT, ".env")):
    """Đọc file .env (KEY=VALUE mỗi dòng) vào biến môi trường, không ghi đè biến đã có. Khung — không cần sửa."""
    if not os.path.exists(path):
        return
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_env()
MODEL_PROVIDER = (os.environ.get("MODEL_PROVIDER") or "fake").strip().lower()
MODEL_NAME = (os.environ.get("MODEL_NAME") or "").strip()
API_KEY = (os.environ.get("API_KEY") or "").strip()


# Gemini và OpenAI dùng chung một dạng API, chỉ khác địa chỉ
URL_OPENAI_STYLE = {
    "openai": "https://api.openai.com/v1/chat/completions",
    "gemini": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
}
URL_CLAUDE = "https://api.anthropic.com/v1/messages"
URL_OLLAMA = "http://localhost:11434/api/chat"


def post_json(url, headers, body, timeout=60):
    """Gửi POST JSON, trả về JSON phản hồi. Lỗi HTTP → RuntimeError kèm lời báo của API."""
    req = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"), method="POST",
        headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError("HTTP %d: %s" % (e.code, e.read().decode("utf-8", "replace")[:300]))


def _messages(system, user):
    return ([{"role": "system", "content": system}] if system else []) + [{"role": "user", "content": user}]


def call_openai_style(system, user):
    data = post_json(URL_OPENAI_STYLE[MODEL_PROVIDER], {"Authorization": "Bearer " + API_KEY},
                     {"model": MODEL_NAME, "messages": _messages(system, user)})
    u = data["usage"]
    # token ra gồm cả token suy nghĩ: có API không tính vào completion_tokens nhưng có trong total_tokens
    tokens_out = max(u.get("completion_tokens") or 0, (u.get("total_tokens") or 0) - u["prompt_tokens"])
    return {"text": data["choices"][0]["message"].get("content") or "",
            "tokens_in": u["prompt_tokens"], "tokens_out": tokens_out}


def call_claude(system, user):
    data = post_json(URL_CLAUDE, {"x-api-key": API_KEY, "anthropic-version": "2023-06-01"},
                     {"model": MODEL_NAME, "max_tokens": 1024, "system": system or "",
                      "messages": [{"role": "user", "content": user}]})
    text = "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")
    u = data["usage"]
    return {"text": text, "tokens_in": u["input_tokens"], "tokens_out": u["output_tokens"]}


def call_ollama(system, user):
    data = post_json(URL_OLLAMA, {}, {"model": MODEL_NAME, "messages": _messages(system, user), "stream": False},
                     timeout=300)
    return {"text": data["message"]["content"],
            "tokens_in": data.get("prompt_eval_count", 0), "tokens_out": data.get("eval_count", 0)}


CALLERS = {"openai": call_openai_style, "gemini": call_openai_style,
           "anthropic": call_claude, "ollama": call_ollama}


@model_call
def call_model(system: str, user: str) -> dict:
    if MODEL_PROVIDER == "fake":
        last = (user.strip().splitlines() or [""])[-1]
        return {"text": "[câu trả lời giả — chưa nối model] " + last[:60], "model": "fake", "tokens_in": 0, "tokens_out": 0}


    if MODEL_PROVIDER not in CALLERS:
        raise NotImplementedError("MODEL_PROVIDER=%s chưa hỗ trợ — dùng một trong: %s"
                                  % (MODEL_PROVIDER, ", ".join(sorted(CALLERS))))
    if not MODEL_NAME:
        raise RuntimeError("Chưa điền MODEL_NAME trong .env")
    if not API_KEY and MODEL_PROVIDER != "ollama":
        raise RuntimeError("Chưa điền API_KEY trong .env")
    r = CALLERS[MODEL_PROVIDER](system, user)
    return {"text": r["text"], "model": MODEL_NAME,
            "tokens_in": int(r["tokens_in"]), "tokens_out": int(r["tokens_out"])}
