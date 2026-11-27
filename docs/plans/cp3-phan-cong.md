# Phân công CP3 — TayDuKy · hạn 10:00 Thứ Bảy 28/11 · 4 điểm

> Nguồn yêu cầu: repo đề `VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon` (commit `b568b95`): README → Checkpoint CP3 · `02-guide.md` giai đoạn 3 và mục 3.4 · `03-rubric.md`.
> Hiện trạng đọc từ repo nhóm tối 27/11. **Giờ trong bảng là đề xuất**, nhóm chỉnh theo thực tế.
> Muộn hoặc thiếu một phần → 0 điểm mốc.

## 1. CP3 phải nộp gì

| # | Phải có | Hiện trạng | Còn thiếu | Phụ trách |
|---|---|---|---|---|
| 1 | `evidence/summary.md`: ≥1 nguồn đạt ngưỡng + ≥5 trích dẫn | Có 5 trích dẫn; khảo sát n = 22 chưa lọc | Lọc còn học viên L3 ngoài nhóm (≥20), giữ log từng câu trả lời, điền mục 1, 4, 5 | Huyền |
| 2 | Bộ câu thử 20–30 câu, ≥5 `kho`, ≥2 `tu_choi`, ≥1/3 từ người dùng / data thật | 16 câu, 0 từ người dùng | Thêm 9–10 câu `nguoi_dung` (tổng 25–26) | Huân viết · Duyên đối chiếu |
| 3 | Bản chạy thử gọi **AI thật** | Chế độ giả, chưa có `.env` | Nối model, `eval --try` thấy token > 0 | Duyên |
| 4 | Video 30 giây | Chưa có | Quay, đăng "Không công khai", mở thử bằng cửa sổ ẩn danh | Linh |
| 5 | `eval/run-N.csv` đã chấm + x/N + run ID | Chưa chạy | Chạy cả bộ, chấm `pass`, `score` | Duyên chạy · Huân chấm |
| 6 | `spec.md` §0–§7 đã commit | §0, §2 trống; §1, §3 còn nháp | Xem mục 2 | Huyền · Linh · Duyên |
| 7 | Ghi phần chưa xong (nếu có) | — | Viết vào form nộp | Huyền |

## 2. Ai sửa file nào

Chỉ người có tên được sửa. Người khác muốn đổi thì nhắn nội dung cho người đó.

| File / mục | Người sửa |
|---|---|
| `codebase/agent.py` | **Linh** |
| `codebase/ai.py`, `codebase/tools.py` | Duyên |
| `spec.md` §0–§3 | Huyền |
| `spec.md` §4, §10 | **Linh** (cả nhóm nhắn dòng changelog cho Linh) |
| `spec.md` §7: chỉ dòng "Kết quả" | Duyên |
| `README.md`, `docs/ai-usage.md` | Linh |
| `eval/benchmark.csv`, `data/DATA_CARD.md` | Huân |
| `eval/README.md` mục 1–3 | Huân |
| `eval/README.md` mục 5–6, `eval/report.md` | Duyên |
| `eval/run-N.csv` | Duyên tạo · Huân điền `pass`, `ghi_chu` |
| `evidence/summary.md`, `evidence/survey/` | Huyền |
| `evidence/interviews/` | Huân |

**Phần "hỏi lại giai đoạn N"** (đang chưa commit trên máy Duyên, đụng `agent.py` và `spec.md` §4, §10): Duyên đẩy lên một nhánh riêng trước 21:30, Linh gộp vào.

## 3. Việc theo người

### Võ Thị Kim Huyền — đội trưởng (bằng chứng, câu chuyện, nộp bài)

| Hạn | Việc | Ra file | Xong khi |
|---|---|---|---|
| 27/11 23:00 | Xuất Sheet khảo sát, lọc học viên L3 ngoài nhóm, tính lại số | `evidence/survey/responses-anon.csv`, `evidence/survey/phan-tich-lan2.md` | N ≥ 20, số khớp log |
| 28/11 08:00 | Hoàn thiện tổng hợp bằng chứng | `evidence/summary.md` | Có kết luận giả thuyết, không còn `__` ở phần đã làm |
| 28/11 08:30 | Viết §0, hoàn thiện §1, §3; lập bảng impact ≥3 hướng | `spec.md` §0–§3 | Số nào cũng có nguồn hoặc ghi *(tự ước tính)* |
| 28/11 09:30 | Nộp form CP3 | — | Nộp bằng mã học viên của đội trưởng |

Khảo sát:
- Không ghi đè `phan-tich-lan1.md`; số sau khi lọc ghi vào file lần 2.
- Bản xuất gốc đặt tên `raw-*.csv` trong `evidence/` để `.gitignore` chặn.
- Trước khi commit `responses-anon.csv`: bỏ cột liên hệ **và đọc từng ô trả lời tự do** để xoá tên người, tên lab coach.
- Dự kiến còn khoảng 21 người, chỉ hơn ngưỡng 20 một người → xin thêm phản hồi ngay tối nay.

Bảng impact:
- Số "hơn 700 học viên L3" trích từ `02-guide.md` mục 4.2 của repo đề.
- Câu 4 chia theo khoảng phút; số phút lấy điểm giữa khoảng phải ghi *(tự ước tính)*.

### Nguyễn Đức Huân (phỏng vấn, bộ câu thử, chấm)

| Hạn | Việc | Ra file | Xong khi |
|---|---|---|---|
| 27/11 20:00–20:45 | Phỏng vấn P1 (người ngoài nhóm) | `evidence/interviews/P1.md` | Có ghi chép, không tên |
| 27/11 22:00 | Viết 9–10 câu từ khảo sát câu 7, 9, C3 và P1 | `eval/benchmark.csv` | `python run.py check` không còn cảnh báo |
| 27/11 23:00 | Sửa đáp án theo đối chiếu của Duyên, **khoá bộ câu**; cập nhật số câu và nguồn; commit | `benchmark.csv`, `DATA_CARD.md`, `eval/README.md` 1–3 | Đã push |
| 27/11 23:00 | Gửi Linh dòng changelog về cách đọc ngưỡng (mục 5) | `spec.md` §10 | Có trong repo **trước khi chạy lượt 1** |
| Tối nay hoặc trước 28/11 08:00 | Phỏng vấn P2, P3 (nguồn thứ hai, +3 điểm R1) | `evidence/interviews/P2.md`, `P3.md` | Đủ 3 file; gửi Huyền tóm tắt |
| 28/11 08:30 | Chấm cột `pass` theo `metric_spec.yaml`; commit | `eval/run-N.csv` | `python run.py score eval/run-N.csv` ra % |

Câu thử từ người dùng:
- Câu 9 là lời phàn nàn: viết lại thành câu hỏi, giữ đúng vấn đề người đó nêu.
- Bỏ mọi tên người (repo công khai).
- `source` bắt đầu bằng `nguoi_dung:` và ghi rõ lấy từ đâu (vd `nguoi_dung: khảo sát câu 7`, `nguoi_dung: P1`).

### Nguyễn Thị Duyên (nối model, đối chiếu đáp án, chạy lượt 1)

| Hạn | Việc | Ra file | Xong khi |
|---|---|---|---|
| 27/11 21:30 | Nối model thật theo `docs/connect-model.md`; push. Kẹt quá 20 phút thì hỏi | `codebase/ai.py`, `.env` (không commit) | `python run.py eval --try` có token > 0 |
| 27/11 21:30 | Đẩy nhánh "giai đoạn N" cho Linh | — | Linh đã nhận |
| 27/11 22:00–22:45 | Đối chiếu `expected` của các câu mới với `data/labs/` | Ghi chú gửi Huân | Mỗi câu mới đã kiểm |
| 27/11 23:30 | Pull bản đã khoá, chạy cả bộ; commit **cả** `run-N.csv` và `traces/run-N.jsonl` | `eval/run-N.csv`, `traces/run-N.jsonl` | Đã push |
| 28/11 07:00 | Chỉ khi lượt tối qua lỗi: chạy lại thành lượt mới | `eval/run-N.csv` mới | Đã push |
| 28/11 08:30–08:45 | Đọc câu trượt cùng Huân; ghi báo cáo và dòng kết quả §7; commit | `eval/report.md`, `eval/README.md` 5–6, `spec.md` §7 | Có x/N và run ID |

- `ai.py` phải trả về `model` đúng tên model thật và token lấy từ API. Thiếu thì khung có thể ghi `run-mock.csv`, không tính là lượt.
- Câu có `error`: không sửa tay file. Chạy lại thành lượt mới, ghi cả hai vào `eval/README.md`, không xoá lượt cũ.

### Vũ Gia Linh (prompt, chặn rủi ro, video, spec §4 và §10)

| Hạn | Việc | Ra file | Xong khi |
|---|---|---|---|
| 27/11 21:30–23:00 | Gộp nhánh "giai đoạn N"; thử model thật với câu thường, mơ hồ, tấn công; sửa prompt / chỗ chặn | `codebase/agent.py` | Nhánh tra lại và chặn chạy với model thật |
| **27/11 23:00** | **Khoá code**: commit, push | — | Không sửa `codebase/` trước khi lượt 1 chạy xong |
| 27/11 23:15 | Ghi dòng changelog Huân gửi và các dòng khác | `spec.md` §10 | Đã push trước 23:30 |
| 28/11 08:00 | Cập nhật phần thật / giả và model đang dùng; commit | `spec.md` §4, `README.md`, `docs/ai-usage.md` | Khớp code |
| 28/11 08:30 | Quay video 30 giây bằng câu thường và câu hỏi lại. **Không dùng T14** hay câu tấn công khác | link | Mở được bằng cửa sổ ẩn danh |

Nếu phải sửa code sau khi lượt 1 đã chạy: ghi §10, và lượt chạy với code mới là một lượt khác.

## 4. Quy tắc chung

- Mỗi máy chạy `python codebase/fetch_labs.py` trước khi chạy bản chạy thử, `eval` hoặc đối chiếu đáp án (`data/labs/` không có trong repo).
- Mỗi người commit ngay khi xong phần mình, `git pull` trước khi commit. Không dồn đến 09:15.

## 5. Ngưỡng khi bộ câu tăng

`metric_spec.yaml` và §7 ghi ví dụ theo bộ 16 câu. **Không sửa hai chỗ đó.** Trước khi chạy lượt 1, ghi vào `spec.md` §10 rằng ngưỡng giữ nguyên theo tỉ lệ, áp lên bộ N câu:

- câu qua ≥ 80% (N = 25 → ≥ 20/25; N = 26 → ≥ 21/26);
- `tra_loi_dung` ≥ 75% câu `answer` · `quyet_dinh_dung` ≥ 80%;
- `trich_dan_co_that` 100% · `tu_choi_dung` 100% · `khong_bia_yeu_cau` 0 câu vi phạm.

## 6. Mốc chung sáng 28/11

| Giờ | Việc |
|---|---|
| 09:00 | Cả nhóm đi lại câu chuyện Pain → Impact → Giải pháp → Đánh giá → Chi phí |
| 09:15 | Kiểm mọi thứ đã push; mở repo, `spec.md`, video bằng cửa sổ ẩn danh |
| 09:30 | Nộp (chừa 30 phút dự phòng) |

**Dời sang CP4:** `python run.py simulate`. Không nằm trong danh sách nộp CP3, và `cost/personas.yaml` còn số mẫu "(ví dụ)" cần thay trước (Linh).

## 7. Luật dễ mất điểm

- Câu thử chỉ được **thêm**; không sửa `expected` cho khớp kết quả, không bỏ câu trượt.
- Không sửa chuẩn "đạt" và `eval/metric_spec.yaml` sau CP2.
- Không commit `.env`, API key, file khảo sát gốc.
- Không bịa người trả lời, trích dẫn, số liệu. Lượt 1 thấp vẫn đủ điểm nếu số thật.
