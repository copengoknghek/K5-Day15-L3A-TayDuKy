"""Tải 5 repo lab L3 khoá K5 (công khai) về data/labs/ rồi đếm file .md và số mục.

Chạy: python codebase/fetch_labs.py
data/labs/ nằm trong .gitignore: không commit nguyên tài liệu khoá.
Mỗi repo ghim đúng một commit để chạy lại ra cùng dữ liệu (ghi ở data/DATA_CARD.md).

Một "mục" = một heading Markdown (#…######) cùng phần chữ bên dưới, tới heading kế tiếp.
Dòng bắt đầu bằng # trong khối code (``` hoặc ~~~) không phải heading.
Phần chữ đứng trước heading đầu tiên được tính là một mục không tên.
Chỉ dùng thư viện chuẩn; cần có lệnh git.
"""
import os
import re
import subprocess
import sys

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LABS_DIR = os.path.join(ROOT, "data", "labs")
ORG_URL = "https://github.com/VinUni-AI20k/"

LABS = [  # (nhãn lab, tên repo, commit ghim — lấy ngày 27/11/2026)
    ("Day4", "K5-L3-Day4-ReactLoopAgent", "147982becd7097cc7930ea09589acb97389e84f4"),
    ("Day07", "K5-L3-Day07-Retrieval-Context-Engineering", "c67ec6292cd6d15e6e6cbaa2c7e7260398bb5a19"),
    ("Day8", "K5-Day8-From-Workflows-to-Agents", "034c6c421c198dae67a9211d15e2587d5a378972"),
    ("Day10", "K5_L3_Day10_PoC-to-Pilot_Gate1_student", "12caf24f37ce1e99eb66b96099248fa5373ed15a"),
    ("Day11", "K5-L3-LAB-Day11-Guardrails-HITL-Responsible-AI", "2e3930fac9dd2dc533211e89e8ccaf90e390d194"),
]

HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def split_sections(text):
    """Cắt một file Markdown thành [(heading, nội dung)]. Mục trước heading đầu tiên có heading ""."""
    sections, heading, body, fence = [], "", [], None

    def close():
        content = "\n".join(body).strip()
        if heading or content:
            sections.append((heading, content))

    for line in text.splitlines():
        mark = FENCE.match(line)
        if fence:
            # khối code đóng khi gặp cùng ký tự, dài không kém, không kèm chữ
            if mark and mark.group(1).startswith(fence) and not mark.group(2).strip():
                fence = None
        elif mark:
            fence = mark.group(1)
        else:
            found = HEADING.match(line)
            if found:
                close()
                heading, body = found.group(2).strip(), []
                continue
        body.append(line)
    close()
    return sections


def markdown_files(folder):
    """Đường dẫn tương đối (dùng /) của mọi file .md trong một repo, bỏ thư mục .git."""
    found = []
    for base, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            if name.lower().endswith(".md"):
                found.append(os.path.relpath(os.path.join(base, name), folder).replace(os.sep, "/"))
    return sorted(found)


def git(folder, *args):
    env = dict(os.environ, GIT_LFS_SKIP_SMUDGE="1", GIT_TERMINAL_PROMPT="0")
    return subprocess.run(["git", "-c", "core.longpaths=true", "-C", folder] + list(args),
                          check=True, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", env=env).stdout.strip()


def head_of(folder):
    if not os.path.isdir(os.path.join(folder, ".git")):
        return None
    try:
        return git(folder, "rev-parse", "HEAD")
    except subprocess.CalledProcessError:  # lần tải trước dở dang
        return None


def fetch(repo, commit):
    """Đảm bảo data/labs/<repo> đang ở đúng commit ghim. Đã đúng thì không tải lại."""
    folder = os.path.join(LABS_DIR, repo)
    if head_of(folder) == commit:
        return folder
    os.makedirs(folder, exist_ok=True)
    if not os.path.isdir(os.path.join(folder, ".git")):
        git(folder, "init", "--quiet")
    git(folder, "fetch", "--quiet", "--depth", "1", ORG_URL + repo + ".git", commit)
    git(folder, "checkout", "--quiet", "--detach", commit)
    return folder


def main():
    total_files = total_sections = 0
    failed = []
    print("%-6s %-8s %5s %5s  %s" % ("lab", "commit", "md", "mục", "repo"))
    for lab, repo, commit in LABS:
        try:
            folder = fetch(repo, commit)
        except FileNotFoundError:
            print("Không tìm thấy lệnh git.")
            return 1
        except subprocess.CalledProcessError as e:
            failed.append(repo)
            print("%-6s lỗi tải %s: %s" % (lab, repo, (e.stderr or "").strip()))
            continue
        files = markdown_files(folder)
        count = 0
        for path in files:
            with open(os.path.join(folder, path), encoding="utf-8-sig", errors="replace") as f:
                count += len(split_sections(f.read()))
        total_files += len(files)
        total_sections += count
        print("%-6s %-8s %5d %5d  %s" % (lab, commit[:7], len(files), count, repo))
    print("%-6s %-8s %5d %5d" % ("TỔNG", "", total_files, total_sections))
    if failed:
        print("Chưa tải được: " + ", ".join(failed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
