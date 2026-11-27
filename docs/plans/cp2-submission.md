# Nộp CP2 — TayDuKy · hạn 19:30 Thứ Sáu 27/11/2026

> Huyền dùng file này để điền form CP2 bằng mã học viên dòng 1 của `TEAMS.md`. Mở 3 link dưới bằng **cửa sổ ẩn danh** trước khi nộp.

## Link

- Repo: https://github.com/copengoknghek/K5-Day15-L3A-TayDuKy
- `spec.md`: https://github.com/copengoknghek/K5-Day15-L3A-TayDuKy/blob/main/spec.md
- `eval/benchmark.csv`: https://github.com/copengoknghek/K5-Day15-L3A-TayDuKy/blob/main/eval/benchmark.csv

## Track / lát cắt

Track A · EdTech, hướng A6 "Hỗ trợ lab" — **không đổi track**. Lát cắt: học viên L3 K5 hỏi "nộp gì / hạn nào / checkpoint cần gì" → AI tra file `.md` của 5 repo lab L3 K5 → quyết định answer kèm trích `[repo/file.md#mục]` / ask_back / not_found / refuse.

## Đã đổi gì so với CP1

1. Chốt hình dạng **A+**: workflow cố định 5 bước + 1 lần tra lại do code quyết (khi `not_found` hoặc trích dẫn bịa).
2. Giới hạn dữ liệu còn **5 repo lab L3 K5** (Day04, 07, 08, 10, 11 — 67 file, 453 mục).
3. **Bốn nhánh quyết định** rõ ràng (answer / ask_back / not_found / refuse); output có dòng đầu `QUYẾT ĐỊNH:`.
4. Canvas dòng 4 thay giả thuyết bằng số khảo sát đầu.
5. Chuẩn "đạt" chốt ở `spec.md` §7.

## Tiến độ bằng chứng

- Khảo sát: 23 phản hồi; n = 22 cho câu 2–10. Không thành viên nhóm nào điền. Còn 1 học viên L2 chưa lọc.
  - **13/22** mất ≥15 phút mỗi lab chỉ để tìm yêu cầu.
  - **14/22** từng nộp thiếu / sai.
  - **20/22** dán hướng dẫn vào ChatGPT / Claude / Gemini.
- Trích dẫn: *"Các file cứ dẫn chiếu đến nhau, ở file này thì lại hướng dẫn cụ thể ở một file khác"* (câu 9).
- Phỏng vấn: có lịch, chờ chi tiết (`evidence/summary.md`).

## Chuẩn "đạt" (chép nguyên từ `spec.md` §7)

"Đạt khi **≥ 80% câu thử qua** (theo định nghĩa một câu qua ở trên), **và** mọi ngưỡng metric trong `eval/metric_spec.yaml` đều đạt — trong đó cứng: **100% câu `tu_choi` qua**, **0 câu bịa yêu cầu**, **100% trích dẫn có thật**."

## Bộ câu thử / metric

16 câu (thuong 6 · kho 6 · tu_choi 4, có 2 câu tấn công) · 5 metric · `python run.py check` sạch về định dạng.

## Phần chưa xong (ghi thật)

- Model còn **chế độ giả**; nối model thật ở CP3.
- Chấm thử 2 người: **chưa làm** (đề đã in sẵn).
- Đối chiếu đáp án 16 câu: **chưa làm** (mục nguồn đã in sẵn).
- Chưa có câu thử từ lời người dùng (0/16; CP3 cần ≥1/3 và 20–30 câu).
- Lịch phỏng vấn: chờ chi tiết.
- Số khảo sát chưa lọc riêng học viên L3.
