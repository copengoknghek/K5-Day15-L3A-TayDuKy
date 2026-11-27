"""Công cụ của bài toán: tra hướng dẫn lab và kiểm trích dẫn. Cả hai chỉ đọc, chỉ dùng thư viện chuẩn.

Nguồn: 5 repo lab trong data/labs/ (tải bằng `python codebase/fetch_labs.py`, mô tả ở data/DATA_CARD.md).
Mã mục (cũng là mã trích dẫn): <repo>/<file>.md#<heading>, viết trong ngoặc vuông ở câu trả lời.
Phần chữ trước heading đầu tiên của file có mã <repo>/<file>.md#(mở đầu).
Heading trùng tên trong cùng một file được gắn mục cha cho khác nhau: …#<mục cha> > <heading>.
Heading cấp 2 trở xuống không có chữ riêng thì lấy nội dung các mục con của nó.
"""
import collections
import functools
import math
import os
import re
import unicodedata

from fetch_labs import LABS, LABS_DIR, markdown_files, split_sections
from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký)

NO_HEADING = "(mở đầu)"
MAX_CHARS = 2500      # cắt mỗi mục khi đưa cho model, để giữ số token vào
HEADING_WEIGHT = 3    # từ nằm ở heading / tên file nặng hơn từ trong nội dung

# Từ hỏi và từ đệm (đã bỏ dấu) — không giúp phân biệt mục nào
STOPWORDS = frozenset(
    "a anh ay bai ban bao can cai cac cho chua co cua da dang de den di duoc gi giup hay "
    "hoi khi khong la lai lam lab minh mot nao nay neu nhu nhung o oi phai ra roi se "
    "sao the thi toi trong tu va vay ve vi voi xin em nhe a an and are for how in is of "
    "on the to what".split())


def _normalize(text):
    """Chữ thường, bỏ dấu tiếng Việt: để gõ không dấu vẫn tra được."""
    text = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return "".join(c for c in text if not unicodedata.combining(c))


def _words(text):
    # "checkpoint 2", "Check point 02", "CP 2", "CP2" đều thành một từ "cp2": mỗi lab viết một kiểu
    text = re.sub(r"\b(?:check[ -]?point|cp)[ #]*0*(\d+)\b", r" cp\1 ", _normalize(text))
    return re.findall(r"[a-z0-9]+", text)


def _key(code):
    """Dạng so sánh của một mã mục: bỏ dấu ** và `, gộp khoảng trắng, không phân biệt hoa thường.
    Giữ nguyên dấu tiếng Việt."""
    code = unicodedata.normalize("NFC", code).replace("`", "").replace("**", "")
    return " ".join(code.split()).casefold()


def _lab_number(lab):
    digits = re.search(r"\d+", str(lab))
    return int(digits.group()) if digits else None


def _with_parents(sections):
    """[(heading, nội dung, cấp)] → [(heading, nội dung, cấp, [heading các mục cha, gần nhất ở cuối])].
    Heading cấp 1 là tên cả file nên không tính là mục cha."""
    stack, result = [], []
    for heading, body, level in sections:
        while stack and stack[-1][0] >= level:
            stack.pop()
        result.append((heading, body, level, [name for _, name in stack]))
        if level >= 2:
            stack.append((level, heading))
    return result


def _file_sections(text):
    """Các mục của một file: [(tên mục dùng trong mã, nội dung, [mục cha])]."""
    sections = _with_parents(split_sections(text))
    seen = collections.Counter(heading for heading, _, _, _ in sections)
    result = []
    for i, (heading, body, level, parents) in enumerate(sections):
        if not body and level >= 2:  # chỉ có mục con: gom chữ của chúng lại
            children = []
            for child, child_body, child_level, _ in sections[i + 1:]:
                if child_level <= level:
                    break
                children.append("%s %s\n%s" % ("#" * child_level, child, child_body))
            body = "\n".join(children).strip()
        name = heading or NO_HEADING
        if seen[heading] > 1 and parents:
            name = "%s > %s" % (parents[-1], name)
        result.append((name, body, parents))
    return result


@functools.lru_cache(maxsize=None)
def _index():
    """Đọc 5 repo một lần: {mã mục: thông tin mục}.
    Thiếu repo thì báo lỗi, không trả danh sách rỗng: nếu không, trợ lý sẽ nói "không có trong tài liệu"
    chỉ vì chưa tải, và lượt đánh giá ra số sai mà không ai biết."""
    missing = [repo for _, repo, _ in LABS if not os.path.isdir(os.path.join(LABS_DIR, repo))]
    if missing:
        raise FileNotFoundError("Chưa có %d repo lab trong data/labs/ — chạy: python codebase/fetch_labs.py"
                                % len(missing))
    index = {}
    for lab, repo, _ in LABS:
        for path in markdown_files(os.path.join(LABS_DIR, repo)):
            with open(os.path.join(LABS_DIR, repo, path), encoding="utf-8-sig", errors="replace") as f:
                sections = _file_sections(f.read())
            for name, body, parents in sections:
                code = "%s/%s#%s" % (repo, path, name)
                # còn trùng cả mục cha thì gộp, để một mã chỉ trỏ tới một chỗ
                entry = index.setdefault(_key(code), {"code": code, "lab": _lab_number(lab), "parents": parents,
                                                     "title": " ".join([path, name] + parents), "body": ""})
                entry["body"] = (entry["body"] + "\n" + body).strip()
    for entry in index.values():
        words = collections.Counter(_words(entry["body"]))
        for word in _words(entry["title"]):
            words[word] += HEADING_WEIGHT
        entry["words"] = words
        entry["length"] = sum(words.values())
    return index


@tool
def search_guides(query: str, lab=None, k: int = 5) -> list:
    """Tên: search_guides — tìm các mục trong hướng dẫn lab khớp từ khoá với câu hỏi (chấm điểm BM25).
    Input: query (str) · lab (None = cả 5 lab, hoặc "Day4", "Day07", 8…) · k (số mục tối đa).
    Output: [{"code": "<repo>/<file>.md#<heading>", "text": nội dung mục}], khớp nhất đứng đầu;
            danh sách rỗng khi không mục nào khớp hoặc lab nằm ngoài 5 lab.
    Tác động ra ngoài: không (chỉ đọc file trong data/labs/)."""
    sections = [e for e in _index().values() if e["body"]]
    average = sum(e["length"] for e in sections) / len(sections)
    if lab is not None:
        number = _lab_number(lab)
        sections = [e for e in sections if e["lab"] == number]

    # "Day 07" trong câu hỏi đã dùng để lọc lab, không tính là từ khoá
    query = re.sub(r"(?i)\b(day|lab|ng[aà]y)\s*0?\d+", " ", unicodedata.normalize("NFC", query))
    # giữ chữ số đơn: "checkpoint 2" khác "checkpoint 1"
    terms = {w for w in _words(query) if w not in STOPWORDS and (len(w) > 1 or w.isdigit())}
    if not sections or not terms:
        return []

    # độ hiếm của từ tính trên đúng tập đang tra
    found_in = {t: sum(1 for e in sections if t in e["words"]) for t in terms}
    rarity = {t: math.log(1 + (len(sections) - n + 0.5) / (n + 0.5)) for t, n in found_in.items() if n}

    def score(entry):
        total = 0.0
        for term, weight in rarity.items():
            count = entry["words"].get(term, 0)
            total += weight * count * 2.2 / (count + 1.2 * (0.25 + 0.75 * entry["length"] / average))
        return total

    ranked = sorted(((score(e), e["code"], e) for e in sections), key=lambda x: (-x[0], x[1]))
    results = []
    for points, code, entry in ranked[:k]:
        if points <= 0:
            break
        text = entry["body"]
        if len(text) > MAX_CHARS:
            text = text[:MAX_CHARS] + "\n…(cắt bớt)"
        if entry["parents"]:  # cho model biết mục này nằm trong mục nào (vd checkpoint mấy)
            text = "Thuộc: %s\n%s" % (" > ".join(entry["parents"]), text)
        results.append({"code": code, "text": text})
    return results


def _citations(text):
    """Mọi đoạn trong ngoặc vuông có nhắc tới file .md. Đếm cả ngoặc lồng nhau, vì heading có thể chứa [ ]."""
    found, opened = [], []
    for i, char in enumerate(text):
        if char == "\n":
            opened = []
        elif char == "[":
            opened.append(i)
        elif char == "]" and opened:
            start = opened.pop()
            inner = text[start + 1:i].strip()
            if opened and ".md#" in text[opened[0]:i].lower():
                continue  # ngoặc nằm trong heading của một trích dẫn đang mở
            if ".md#" in inner.lower():
                found.append(inner)
            elif inner.lower().endswith(".md") and text[i + 1:i + 2] != "(":
                found.append(inner)  # trích file mà không chỉ mục nào (không tính link Markdown)
    return found


@tool
def verify_citations(text: str) -> dict:
    """Tên: verify_citations — kiểm mọi trích dẫn [<repo>/<file>.md#<heading>] có thật trong data/labs/ không.
    Input: text (str), câu trả lời của model.
    Output: {"ok": không có trích dẫn sai, "invalid": [mã sai], "count": số trích dẫn tìm thấy}.
            Câu không có trích dẫn nào vẫn "ok": nơi gọi tự kiểm count khi câu trả lời bắt buộc có nguồn.
            Chỉ kiểm mục CÓ TỒN TẠI, không kiểm nội dung câu trả lời có đúng với mục đó.
    Tác động ra ngoài: không (chỉ đọc)."""
    index = _index()
    cited = _citations(text)
    invalid = [c for c in cited if _key(c) not in index]
    return {"ok": not invalid, "invalid": invalid, "count": len(cited)}


def _try(argv):
    """Chạy thử bằng tay, không gọi model:
    python codebase/tools.py "câu hỏi" [lab]
    python codebase/tools.py --verify "câu trả lời có [mã trích dẫn]" """
    import sys
    for stream in (sys.stdout, sys.stderr):
        stream.reconfigure(encoding="utf-8", errors="replace")
    if argv[:1] == ["--verify"] and len(argv) == 2:
        print(verify_citations(argv[1]))
    elif argv and not argv[0].startswith("-"):
        results = search_guides(argv[0], lab=argv[1] if len(argv) > 1 else None)
        if not results:
            print("Không mục nào khớp.")
        for number, found in enumerate(results, 1):
            preview = " ".join(found["text"].split())[:200]
            print("%d. [%s]\n   %s\n" % (number, found["code"], preview))
    else:
        print(_try.__doc__)


if __name__ == "__main__":
    import sys
    _try(sys.argv[1:])
