"""Giao diện web cho bản chạy thử. Chỉ dùng thư viện chuẩn, không sửa luồng trong agent.py.

Chạy trên máy:  python codebase/web.py          → http://localhost:8000
Deploy:         máy chủ đặt biến PORT, web tự nghe trên 0.0.0.0 (xem docs/deploy.md).

API key chỉ nằm ở máy chủ (.env hoặc biến môi trường). Ai có link đều hỏi được bằng key của nhóm,
nên có giới hạn: độ dài câu hỏi, số câu mỗi phút mỗi địa chỉ, tổng số câu mỗi ngày.
"""
import collections
import csv
import glob
import json
import os
import re
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import ai                                    # noqa: E402  (đọc .env khi nạp)
from agent import answer, next_lab, split_decision  # noqa: E402
from fetch_labs import LABS, ORG_URL         # noqa: E402
from tools import _index                     # noqa: E402

STATIC = {  # chỉ phục vụ đúng các file này
    "/": ("index.html", "text/html"),
    "/style.css": ("style.css", "text/css"),
    "/bot": ("bot.html", "text/html"),
    "/common.js": ("common.js", "text/javascript"),
    "/home.js": ("home.js", "text/javascript"),
    "/bot.js": ("bot.js", "text/javascript"),
    "/hero.png": ("hero.png", "image/png"),
    "/bot.png": ("bot.png", "image/png"),
}
MAX_CHARS = 500
PER_MINUTE = int(os.environ.get("WEB_PER_MINUTE") or 6)
PER_DAY = int(os.environ.get("WEB_PER_DAY") or 200)

_lock = threading.Lock()
_recent = collections.defaultdict(collections.deque)  # địa chỉ → giờ các câu hỏi trong 60 giây
_day = {"date": "", "count": 0}


def over_limit(client):
    """Lời báo nếu vượt giới hạn, chuỗi rỗng nếu được hỏi (và tính luôn câu này)."""
    now, today = time.time(), time.strftime("%Y-%m-%d")
    with _lock:
        if _day["date"] != today:
            _day.update(date=today, count=0)
            _recent.clear()
        if _day["count"] >= PER_DAY:
            return "Bản demo đã hết lượt hỏi hôm nay. Bạn quay lại vào ngày mai nhé."
        times = _recent[client]
        while times and now - times[0] > 60:
            times.popleft()
        if len(times) >= PER_MINUTE:
            return "Bạn hỏi hơi nhanh. Chờ khoảng một phút rồi hỏi tiếp nhé."
        times.append(now)
        _day["count"] += 1
    return ""


def latest_run():
    """Số liệu của lượt đánh giá mới nhất (eval/run-N.csv); None nếu chưa có lượt nào."""
    runs = []
    for path in glob.glob(os.path.join(ROOT, "eval", "run-*.csv")):
        m = re.fullmatch(r"run-(\d+)\.csv", os.path.basename(path))
        if m:
            runs.append((int(m.group(1)), path))
    if not runs:
        return None
    number, path = max(runs)
    previous = None  # số câu đạt của lượt đã chấm ngay trước, để so
    for older, older_path in sorted(runs, reverse=True):
        if older < number:
            with open(older_path, encoding="utf-8-sig", newline="") as f:
                marks = [(r.get("pass") or "").strip() for r in csv.DictReader(f)]
            if marks and all(m in ("0", "1") for m in marks):
                previous = marks.count("1")
                break
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    types, passed = {}, []
    for row in rows:
        expected = row["expected"].split("·")[0].strip()
        decision, _ = split_decision(row["output"])
        # cùng cách tính của metric quyet_dinh_dung: T16 nhận refuse hoặc not_found
        right = decision == expected or (row["id"] == "T16" and decision in ("refuse", "not_found"))
        entry = types.setdefault(row["type"], {"right": 0, "passed": 0, "total": 0})
        entry["total"] += 1
        entry["right"] += int(right)
        entry["passed"] += int((row.get("pass") or "").strip() == "1")
        passed.append((row.get("pass") or "").strip())
    graded = bool(passed) and all(p in ("0", "1") for p in passed)
    return {"run": number, "total": len(rows), "types": types,
            "right": sum(t["right"] for t in types.values()),
            "passed": passed.count("1") if graded else None,
            "previous": previous}


def stats():
    index = _index()
    repos = {}
    for entry in index.values():
        repo, path = entry["code"].split("#", 1)[0].split("/", 1)
        repos.setdefault(repo, set()).add(path)
    labs = [{"label": "Day%02d" % int(re.sub(r"\D", "", label)), "repo": repo,
             "url": "%s%s/tree/%s" % (ORG_URL, repo, commit), "files": len(repos.get(repo, ()))}
            for label, repo, commit in LABS]
    return {"labs": labs, "files": sum(lab["files"] for lab in labs), "sections": len(index),
            "model": ai.MODEL_NAME if ai.MODEL_PROVIDER != "fake" else None, "eval": latest_run()}


class Handler(BaseHTTPRequestHandler):
    server_version = "TayDuKy"
    sys_version = ""

    def _send(self, code, body, kind="application/json"):
        self.send_response(code)
        self.send_header("Content-Type", kind if kind.startswith("image/") else kind + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def _json(self, code, data):
        self._send(code, json.dumps(data, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/api/stats":
            try:
                return self._json(200, stats())
            except Exception as e:
                print("lỗi /api/stats: %r" % e, file=sys.stderr)
                return self._json(500, {"error": "Chưa đọc được tài liệu lab trên máy chủ."})
        if path not in STATIC:
            return self._json(404, {"error": "Không có trang này."})
        name, kind = STATIC[path]
        with open(os.path.join(HERE, "static", name), "rb") as f:
            self._send(200, f.read(), kind)

    do_HEAD = do_GET

    def do_POST(self):
        if self.path != "/api/ask":
            return self._json(404, {"error": "Không có địa chỉ này."})
        # chỉ nhận JSON: trang web khác không gửi hộ được bằng form
        if not (self.headers.get("Content-Type") or "").startswith("application/json"):
            return self._json(415, {"error": "Cần gửi JSON."})
        try:
            length = int(self.headers.get("Content-Length") or 0)
            if not 0 < length <= 8192:
                raise ValueError
            data = json.loads(self.rfile.read(length).decode("utf-8"))
            question = data["question"].strip()
            lab = data.get("lab")  # số lab nhớ trong phiên của trình duyệt này (giống app.py)
            lab = lab if type(lab) is int else None
        except (ValueError, KeyError, TypeError, AttributeError):
            return self._json(400, {"error": "Câu hỏi gửi lên không đọc được."})
        if not question or len(question) > MAX_CHARS:
            return self._json(400, {"error": "Câu hỏi cần từ 1 đến %d ký tự." % MAX_CHARS})
        # sau proxy của nhà cung cấp, địa chỉ thật là phần tử cuối proxy thêm vào
        forwarded = (self.headers.get("X-Forwarded-For") or "").split(",")[-1].strip()
        client = forwarded if os.environ.get("PORT") and forwarded else self.client_address[0]
        blocked = over_limit(client)
        if blocked:
            return self._json(429, {"error": blocked})
        try:
            output = answer(question, lab_context=lab)["output"]
        except Exception as e:  # không gửi chi tiết lỗi ra ngoài; xem ở log máy chủ
            print("lỗi khi trả lời: %s: %s" % (type(e).__name__, e), file=sys.stderr)
            return self._json(502, {"error": "Chưa lấy được câu trả lời. Bạn thử lại sau ít phút."})
        decision, body = split_decision(output)
        self._json(200, {"decision": decision, "text": body, "lab": next_lab(question, lab)})


def main():
    online = os.environ.get("PORT")
    host, port = ("0.0.0.0", int(online)) if online else ("127.0.0.1", 8000)
    _index()  # thiếu data/labs thì báo ngay lúc khởi động
    server = ThreadingHTTPServer((host, port), Handler)
    print("Web chạy ở http://%s:%d · model: %s" % ("localhost" if not online else host, port,
                                                  ai.MODEL_NAME if ai.MODEL_PROVIDER != "fake" else "chế độ giả"))
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nĐã dừng.")


if __name__ == "__main__":
    main()
