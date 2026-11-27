# Data card — dữ liệu bản chạy thử dùng

> Bản đầu ở CP2, đủ ở CP3. Không commit nguyên tài liệu khoá: repo lab chỉ được clone vào `data/labs/` (có trong `.gitignore`).

## Dataset 1 · Tài liệu hướng dẫn của 5 repo lab L3 khoá K5

| | |
|---|---|
| Dùng để làm gì | Nguồn cho 2 công cụ `search_guides`, `verify_citations` (`codebase/tools.py`; `list_guides`, `get_section` để CP3) · đáp án chuẩn của bộ câu thử |
| Từ đâu | Repo công khai của khoá trên GitHub (org VinUni-AI20k): `K5-L3-Day4-ReactLoopAgent`, `K5-L3-Day07-Retrieval-Context-Engineering`, `K5-Day8-From-Workflows-to-Agents`, `K5_L3_Day10_PoC-to-Pilot_Gate1_student`, `K5-L3-LAB-Day11-Guardrails-HITL-Responsible-AI` |
| Xử lý những bước gì | `python codebase/fetch_labs.py`: tải từng repo về `data/labs/` và **ghim đúng commit** ghi ở dòng "Phiên bản" (chạy lại ra cùng dữ liệu) · chỉ đọc file `.md` (bỏ `.git/`, code, notebook, ảnh), UTF-8 có bỏ BOM · cắt theo heading Markdown `#`–`######` thành mục, dòng `#` trong khối code ``` / ~~~ không tính là heading, phần chữ trước heading đầu tiên là mục `(mở đầu)` (`split_sections` trong `codebase/fetch_labs.py`) · mã mục `<repo>/<file>.md#<heading>`; heading trùng tên trong một file được gắn mục cha: `…#<mục cha> > <heading>` · khi tra (`codebase/tools.py`): bỏ dấu tiếng Việt, "checkpoint 2" = "CP2", chấm điểm BM25, mỗi mục đưa model tối đa 2500 ký tự |
| Số dòng / số đoạn | 5 repo · **67** file `.md` · **453** mục — Day04: 7 file / 55 mục · Day07: 17 / 51 · Day08: 23 / 113 · Day10: 14 / 148 · Day11: 6 / 86 (in bởi `python codebase/fetch_labs.py`, chạy lại ra cùng số) |
| Phiên bản / ngày lấy | Commit mới nhất của nhánh mặc định, lấy ngày 27/11/2026. Hash: Day04 `147982b` · Day07 `c67ec62` · Day08 `034c6c4` · Day10 `12caf24` · Day11 `2e3930f` |
| Nhãn | thật (tài liệu khoá, công khai) |
| Giới hạn | Chỉ 5 repo L3 của K5, không có repo K4 hay L2 · chỉ đọc `.md`, bỏ qua code, notebook, ảnh · tài liệu có thể đổi sau ngày lấy · không commit nguyên văn vào repo nhóm |

## Dataset 2 · Bộ câu thử `eval/benchmark.csv`

| | |
|---|---|
| Dùng để làm gì | Đo bản chạy thử (`run.py eval`) |
| Từ đâu | T01–T16 (CP2): nhóm tự viết theo 4 lớp chỗ khó. T17–T26 (CP3): viết lại từ vấn đề **thật** người dùng nêu — khảo sát câu 7 (sai tên repo, sai chỗ nộp link, lỗi email trong file report), câu 9 (file dẫn chiếu nhau, tên repo khác giữa LMS / repo / lab coach), câu 10 (làm nhanh thì cho AI làm hết), C3 (lab coach kể câu "mở cái này sao chạy") và phỏng vấn P1 (nhóm bỏ sót CP2, mở 4–5 tab) — mỗi vấn đề đặt vào một lab cụ thể, bỏ mọi tên người; cột `source` ghi `nguoi_dung: khảo sát câu …` / `nguoi_dung: P1`. Đáp án chuẩn lấy từ Dataset 1, mã mục đã kiểm bằng `python codebase/tools.py --verify` |
| Số dòng | **26 câu** (khoá ở CP3): thuong 9 · kho 11 · tu_choi 6 · nhãn mong đợi answer 16 · ask_back 1 · not_found 3 · refuse 6 (T16 nhận cả not_found) · theo lab: Day04 6 · Day07 5 · Day08 7 · Day10 5 · Day11 2 · không nói lab 1 |
| Nhãn | `tu_viet` 16 câu (T01–T16, CP2) · `nguoi_dung` 10 câu (T17–T26, CP3: khảo sát 9 câu, P1 1 câu; T22 dùng cả khảo sát và P1) → từ người dùng 10/26 (≥ 1/3), in bởi `python run.py check` |
| Giới hạn | Đáp án chuẩn do nhóm đọc tay từ tài liệu; người thứ hai (Duyên) đối chiếu từng câu mới trước khi khoá · câu `nguoi_dung` là vấn đề người dùng nêu được **nhóm viết lại** thành câu hỏi về một lab, không phải nguyên văn câu họ hỏi · khảo sát chưa lọc học viên L3 ngoài nhóm (xem `evidence/survey/`), P1 là một người · chỉ phủ 5 lab, Day11 ít câu (2) |
