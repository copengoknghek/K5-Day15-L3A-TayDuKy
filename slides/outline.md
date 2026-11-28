# Dàn slide → lấy số từ file nào

> Làm ở guide bước 5.1. Luật: **không có bằng chứng thì không có slide** — mỗi trang ≥1 con số / trích dẫn có nguồn / kết quả đo.
> Xuất PDF thành `demo-slides.pdf` ở thư mục gốc repo, nộp tại CP4 14:30 Thứ Bảy 28/11. Nộp PDF, không nộp link.
> Bản dựng slide: `slides/deck.html` (mở bằng Chrome → In → Lưu dưới dạng PDF, khổ ngang, bỏ lề) → lưu thành `demo-slides.pdf` ở gốc repo.

| # | Trang | Có gì | Số lấy từ | Xong |
|---|---|---|---|---|
| 1 | Người dùng & pain | Ai · việc gì · chỗ đau + số và trích dẫn | `evidence/summary.md` | ☑ |
| 2 | Vì sao chọn bài này | Bảng impact rút gọn + hướng bị loại | `spec.md` §2 | ☑ |
| 3 | Giải pháp | Lát cắt một câu · sơ đồ · AI tự làm đến đâu, vì sao | `spec.md` §4 | ☑ *(soát lại nếu Linh đổi §4 trước 11:45)* |
| 4 | Demo live | 1 trường hợp thường + 1 trường hợp khó (lấy từ bộ câu thử); mạng hỏng → video dự phòng | `eval/benchmark.csv` | ☑ *(chốt câu với Duyên sau khi khoá code)* |
| 5 | **Đánh giá thế nào** | Dataset · bộ câu thử · metric · lượt 1 → lượt 2 so với chuẩn "đạt" (kèm run ID) · lỗi chính | `eval/README.md`, `eval/report.md` | ☑ |
| 6 | **Chi phí khi dùng thật** | Chi phí / task thành công · 3 kịch bản · so với impact | `cost/cost-estimate.md` | ☐ chờ `simulate` (Linh) |
| 7 | Kết luận | Go / iterate / stop — dẫn số ở trang 1, 5, 6 | — | ◐ khung xong, chờ số trang 5, 6 |
| 8 | Nếu có thêm 1 tuần | 2–3 việc, trỏ về lỗi còn lại / phản hồi người dùng | `eval/report.md` mục 4 · `validation/log.md` | ☐ chờ Huân / Duyên |

---

## Nội dung từng trang (bản nháp để dựng slide)

### Trang 1 — Người dùng & pain *(nói: Huyền)*

- **Ai:** học viên L3 (L3A, L3B) khoá AI20K K5, đang làm lab theo nhóm trên lớp.
- **Việc:** nộp đúng và đủ bài lab (tên repo, file, hạn, checkpoint) trong buổi lab.
- **Vướng:** yêu cầu rải ở **6–23 file `.md`** mỗi repo lab, file dẫn chiếu nhau (`data/DATA_CARD.md`).
- **Số (khảo sát `N = 23` học viên L3 ngoài nhóm — `evidence/summary.md` §2):**
  - **14/23 (60,9%)** mất ≥15 phút mỗi lab chỉ để tìm yêu cầu
  - **16/23 (69,6%)** từng nộp thiếu / sai ≥1 lần
  - **13/23 (56,5%)** mở ≥4 file · **12/23 (52,2%)** từng thấy hai file ghi khác nhau
  - **20/23 (87,0%)** đang dán hướng dẫn vào ChatGPT / Claude / Gemini — vẫn nộp sai
- **Kiểm lại bằng phỏng vấn 3 người ngoài nhóm:** 3/3 gặp yêu cầu rải nhiều file · 3/3 nhóm từng nộp thiếu / suýt thiếu · 2/3 thấy AI chung bỏ sót điều kiện phụ.
- **Trích dẫn (chọn 2):**
  - *"Các file cứ dẫn chiếu đến nhau, ở file này thì lại hướng dẫn cụ thể ở một file khác"* — S16, khảo sát
  - *"Code chạy được không có nghĩa là checklist nộp bài đã đủ."* — P2, phỏng vấn

### Trang 2 — Vì sao chọn bài này *(nói: Huyền)*

| Hướng | Người gặp | Impact / tháng | Chọn? |
|---|---|---|---|
| **Tra yêu cầu nộp & checkpoint có trích `file#mục`** | ~700 học viên L3 · 60,9% mất ≥15' | **~3.290 giờ** (bảo thủ ~1.278 giờ) | **Chọn** |
| Giải thích nội dung kỹ thuật / code lab | 6/23 (26,1%) | ~549–1.098 giờ *(tự ước tính)* | Loại — dễ thành làm hộ bài, khó chấm đúng/sai |
| Bot trả lời trên Discord / Zalo lớp | 3/23 (13,0%) | ~182–273 giờ *(tự ước tính)* | Loại — ít người dùng kênh này, không được gắn bot vào Discord thật |

- **Công thức:** 700 học viên × 12 lab/tháng × 23,5 phút = **197.400 phút ≈ 3.290 giờ/tháng** (~4,7 giờ/học viên/tháng).
- Nguồn: 700 — `02-guide.md` 4.2 · 12 lab/tháng *(tự ước tính)* · 23,5' — trung bình điểm giữa khoảng câu 4 khảo sát *(tự ước tính)* (`spec.md` §2).

### Trang 3 — Giải pháp *(nói: Linh)*

- **Lát cắt:** học viên hỏi "nộp gì / hạn nào / checkpoint X cần gì" → AI tra tài liệu `.md` của 5 repo lab rồi **quyết định**: `answer` kèm `[repo/file.md#mục]` · `ask_back` · `not_found` ("hỏi lab coach") · `refuse` → học viên biết đúng yêu cầu mà không tự gom từ nhiều file.
- **Hình dạng: workflow cố định A+** (5 bước, 1 lần tra lại do **code** quyết): ① nhận diện lab → ② `search_guides` (BM25, 67 file / 453 mục) → ③ `gpt-4o-mini` chọn 1 trong 4 quyết định → ④ code kiểm trích dẫn + chặn số / tên ngoài căn cứ → ⑤ không qua thì tra lại 1 lần, vẫn hỏng thì câu an toàn.
- **Vì sao không agent:** không bước nào cần model tự chọn công cụ; mọi câu hỏi đi cùng một đường.
- **Mức tự động:** AI tự trả lời khi có căn cứ, chuyển lab coach khi không chắc. Không có công cụ nào tác động ra ngoài. Lab coach giữ: gia hạn, ngoại lệ, điểm, tài liệu mâu thuẫn.
- **Không làm:** không đưa lời giải · không trả lời điểm / gia hạn · không nộp thay · không trả lời ngoài 5 lab.

### Trang 4 — Demo live *(nói: Duyên)*

| | Câu | Từ bộ thử | Kỳ vọng thấy | Lượt 1 |
|---|---|---|---|---|
| **Thường** | "Lab Day04: bài này làm cá nhân hay nhóm? Mình học L3A thì repo nộp đặt tên thế nào?" | T01 (`thuong`) | `answer` · bài cá nhân · mẫu `K5-L3A-DAY04-[HoVaTen]-[MSSV]-ReactLoopAgent` · có trích dẫn mở được | qua |
| **Khó** | "Lab Day07: bài lab này chiếm bao nhiêu phần trăm tổng điểm của khoá?" | T11 (`kho`, lớp 1 — tài liệu không ghi) | `not_found` · không bịa % · "hỏi lab coach" — đúng lỗi đắt nhất mà hệ thống chặn | qua |
| *Dự phòng khó* | "bước tiếp theo là gì vậy?" | T07 (`kho`, lớp 2 — mơ hồ) | `ask_back` hỏi lại lab nào | qua |

- Mạng hỏng → chiếu video dự phòng (link trong `README.md`).
- Câu lạ của giám khảo: nếu không có trong tài liệu → hệ thống trả `not_found`, không đoán.
- *Chốt lại 2 câu với Duyên sau khi khoá code 11:45 và chạy thử trên bản khoá.*

### Trang 5 — Đánh giá thế nào *(nói: Huân)*

- Dataset: 5 repo lab · 67 file · 453 mục (`data/DATA_CARD.md`) · bộ thử **26 câu** (thường 9 · khó 11 · từ chối 6; 10/26 từ người dùng).
- 5 metric · chuẩn "đạt" (chốt CP2): **≥80% câu qua (≥21/26)** + 100% `tu_choi` + 0 bịa + 100% trích dẫn có thật.
- **Lượt 1 → Lượt 2:**
  - Lượt 1 (`run-1@20261127-233523`): **13/26 (50%)** · `thuong` 3/9 · `kho` 4/11 · `tu_choi` 6/6 · 0 bịa · 100% trích dẫn có thật.
  - Lượt 2 (`run-5@20261128-105400`, 0 lỗi kỹ thuật): **18/26 (69%)** · `thuong` 8/9 · `kho` 4/11 · `tu_choi` 6/6 · 0 bịa · 100% trích dẫn có thật · **chưa đạt chuẩn ≥21/26** (`quyet_dinh_dung` 19/26 → **24/26** đạt ngưỡng).
- **Cải tiến & lỗi chính:**
  - Nhóm lỗi đã nhắm ("đáng lẽ `answer` → `not_found`"): **7 → 1** (còn T12); tốt lên 6 câu (T05, T06, T18, T19, T21, T26); tệ đi 1 câu (T23: `answer` thay vì `not_found`).
  - Lỗi chính còn lại: 6 câu `answer` thiếu ý / lạc (T03, T08, T09, T10, T17, T22), T12 còn `not_found`, T23 sai nhánh. *(Lưu ý: cải tiến có chạy dò trên bộ câu thử, chưa có tập giữ riêng.)*

### Trang 6 — Chi phí khi dùng thật *(nói: Linh — chờ `simulate`)*

- Chi phí / task thành công: __ (`gpt-4o-mini`) · __ (`gpt-5.4-mini`, giả định cùng tỉ lệ đạt)
- 3 kịch bản / tháng: thấp __ · cơ sở __ · cao __
- So impact: chi phí __ / người / tháng ↔ ~4,7 giờ / học viên / tháng đang mất (`spec.md` §2)

### Trang 7 — Kết luận: Go / Iterate / Stop *(nói: Huyền)*

**Luật quyết định (đặt trước khi có số lượt 2):**

| Kết luận | Khi nào |
|---|---|
| **Go** | Lượt 2 đạt chuẩn (≥21/26) **và** 3 ngưỡng cứng giữ (0 bịa, 100% từ chối, 100% trích dẫn có thật) **và** chi phí / người / tháng nhỏ hơn rất nhiều so với giá trị ~4,7 giờ / người / tháng |
| **Iterate** | Ngưỡng cứng giữ (an toàn) nhưng câu qua < 80% — trợ lý chưa bịa, nhưng còn hay nói "không thấy" hoặc trả lời thiếu |
| **Stop** | Có câu bịa yêu cầu nộp / trích dẫn giả, hoặc chi phí vượt giá trị tiết kiệm được |

- **Đã biết:** pain thật và lớn (trang 1: 60,9% mất ≥15', 69,6% nộp sai) · lượt 2: **18/26 (69%)** < 80%, nhưng giữ trọn 3 ngưỡng cứng (0 bịa · 6/6 từ chối · 26/26 trích dẫn có thật).
- **Kết luận:** __ *(chờ số chi phí trang 6 của Linh để chốt cuối — theo luật trên đang là **Iterate** nếu chi phí hợp lý)*

### Trang 8 — Nếu có thêm 1 tuần *(nói: Duyên — chờ `eval/report.md` mục 4, `validation/log.md`)*

1. __
2. __
3. __

---

**Trước khi lên:** tải repo về một máy khác (hoặc thư mục mới), chạy theo mục "Chạy trong 3 phút" của `README.md` · `.env` có trên máy demo, đã gọi thử 1 câu trong vòng 1 giờ trước giờ demo · video dự phòng mở được bằng cửa sổ ẩn danh · biết bản chạy thử sẽ làm gì với **1 câu thử lạ** của giám khảo.

Ai nói trang nào (mỗi người ≥1 phần):

| Trang | Người nói |
|---|---|
| 1 · Người dùng & pain | Võ Thị Kim Huyền |
| 2 · Vì sao chọn bài này | Võ Thị Kim Huyền |
| 3 · Giải pháp | Vũ Gia Linh |
| 4 · Demo live | Nguyễn Thị Duyên |
| 5 · Đánh giá | Nguyễn Đức Huân |
| 6 · Chi phí | Vũ Gia Linh |
| 7 · Kết luận | Võ Thị Kim Huyền |
| 8 · Nếu có thêm 1 tuần | Nguyễn Thị Duyên |
