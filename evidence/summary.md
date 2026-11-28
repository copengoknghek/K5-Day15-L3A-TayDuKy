# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Mạnh nhất: đào data ra insight → hỏi người dùng để kiểm lại (hoặc ngược lại).

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☐ *(không dùng làm nguồn chính; dùng bổ trợ đếm số file `.md` trên 5 repo lab trong `data/DATA_CARD.md`)* | `data/DATA_CARD.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☑ Đạt ngưỡng (3 học viên L3 ngoài nhóm) | `evidence/interviews/P1.md`, `P2.md`, `P3.md` |
| **Khảo sát (≥20 người ngoài nhóm, đúng người dùng)** | **☑ Đạt ngưỡng (`N = 23` học viên L3 ngoài nhóm)** | `evidence/survey/responses-anon.csv`, `evidence/survey/phan-tich-lan2.md` *(lần 1: `phan-tich-lan1.md`)* |

## 2. Số chính

- **Khảo sát (nguồn chính — lần 2, đã lọc từ Sheet tối 27/11/2026):** tổng **25 phản hồi**, không thành viên nào của nhóm TayDuKy điền. Sau khi loại 1 học viên L2 (`S03`) và tách riêng 1 lab coach (`S06`), tập mẫu chính gồm **`N = 23` học viên L3 ngoài nhóm** (20 L3A · 3 L3B; 23/23 làm lab trong tuần này).
  - Mất **≥15 phút** mỗi lab chỉ để tìm/hiểu yêu cầu (không tính code): **14/23 (60,9%)** · mất ≥30 phút: **5/23 (21,7%)** · trung vị 15–30 phút/lab *(trung bình trọng số theo điểm giữa khoảng ≈ 23,5 phút/lab, tự ước tính)*.
  - Từng làm **thiếu / sai** yêu cầu lab ≥1 lần: **16/23 (69,6%)** · từng bị ≥2 lần: **10/23 (43,5%)**.
  - Mở **≥4 file** hướng dẫn trong buổi lab gần nhất: **13/23 (56,5%)** · mở ≥6 file: **7/23 (30,4%)**.
  - Từng thấy **hai file ghi khác nhau** về cùng một việc: **12/23 (52,2%)**.
  - Cách xoay xở hiện tại khi chưa chắc yêu cầu (chọn nhiều): **dán hướng dẫn vào ChatGPT/Claude/Gemini 20/23 (87,0%)** · đọc lại / tìm trong file **15/23 (65,2%)** · hỏi bạn cùng nhóm **10/23 (43,5%)** · hỏi lab coach / TA **4/23 (17,4%)** · hỏi Discord/Zalo **3/23 (13,0%)** · đoán rồi làm tiếp **3/23 (13,0%)**.
  - **Góc nhìn phụ từ Lab coach (`S06`, n = 1, tách khỏi `N = 23`):** nhận **11–20 câu hỏi / ca** mà đáp án đã có trong file hướng dẫn, mất **10–30 phút / ca** để trả lời.
  - Chi tiết log ẩn danh và bảng gắn nhãn câu 9: [evidence/survey/responses-anon.csv](survey/responses-anon.csv) · [evidence/survey/phan-tich-lan2.md](survey/phan-tich-lan2.md).
- **Phỏng vấn (nguồn kiểm lại — 3 học viên ngoài nhóm, `evidence/interviews/P1.md`–`P3.md`):** **3/3** người gặp pain yêu cầu nằm rải nhiều file dẫn chiếu nhau · **3/3** kể nhóm từng làm thiếu / suýt nộp thiếu yêu cầu (P1 bỏ sót CP2, P2 thiếu phần ghi kết quả kiểm thử, P3 thiếu minh chứng) · **2/3** (P2, P3) từng thấy AI chung bỏ sót điều kiện phụ khi tóm tắt. Chỉ P1 đã điền khảo sát; P2, P3 tiếp cận ngoài danh sách khảo sát.

Phỏng vấn nhiều vai thì đếm theo từng vai, không cộng chung (cả 3 người cùng vai học viên L3).

| | Vai | Gặp pain? | Số lần / 1 tháng qua | Lần gần nhất mất | Đang xoay xở bằng |
|---|---|---|---|---|---|
| P1 | Học viên L3A (đã điền khảo sát) | Có | không hỏi — "gần như buổi nào cũng cần ngồi đọc xem phải nộp gì" | tự đọc thường >30 phút | dán file `.md` vào ChatGPT để tổng hợp, ít kiểm lại |
| P2 | Học viên L3A (chưa điền khảo sát) | Có | không hỏi | ~20 phút gom checklist (10–15 repo quen · 25–30 repo mới); +15–20 phút bổ sung phần thiếu | checklist riêng + ChatGPT lập bảng có dẫn nguồn, tự mở file kiểm lại |
| P3 | Học viên L3B (ngoài danh sách khảo sát) | Có | không hỏi | ghi chép có hai mức: "hơn 1 tiếng, repo quen ~45 phút" (câu 5) và "30–40 phút repo mới, 20–30 phút repo quen" (phần số); +20–25 phút bổ sung minh chứng | chia nhau đọc từng file, Claude gom ý, Ctrl+F kiểm lại |

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

*(Câu 1–8 chép nguyên văn từ [evidence/survey/responses-anon.csv](survey/responses-anon.csv); câu 9–12 từ ghi chép phỏng vấn `evidence/interviews/`. Đã bỏ tên.)*

1. *"Các file cứ dẫn chiếu đến nhau, ở file này thì lại hướng dẫn cụ thể ở một file khác"* — `S16` (Học viên L3A, khảo sát câu 9)
2. *"Hướng dẫn dài và tốn kha khá thời gian để hiểu, cộng với việc chạy song song với thời gian Checkpoint nên bị chậm tiến độ"* — `S05` (Học viên L3A, khảo sát câu 9)
3. *"Sai cách đặt tên repo giữa Lms và repo, bên cạnh đó hướng dẫn sai với lab coach nói"* — `S23` (Học viên L3A, khảo sát câu 9)
4. *"Không biết có bị gì không nhưng tôi điền email cá nhân thay vì là email trường vào file report_team.md"* — `S05` (Học viên L3A, khảo sát câu 7)
5. *"Sai chỗ link nộp bài hôm lab 1 do làm mini lab"* — `S23` (Học viên L3A, khảo sát câu 7)
6. *"Ghi sai tên repo"* — `S08` (Học viên L3A, khảo sát câu 7)
7. *"Nếu tôi làm nhanh để kịp tiến độ thì coi như là cho AI làm hết, bản thân chỉ đọc hiểu, không được thực hành"* — `S05` (Học viên L3A, khảo sát câu 10)
8. *"cái này làm sao vậy, ủa mở cái này sao chạy sao"* — `S06` (Lab coach / TA, khảo sát câu C3)
9. *"Thường phải mở 4-5 tab chrome vì các file cứ liên kết chỉ tới nhau"* — `P1` (Học viên L3A, phỏng vấn)
10. *"Code chạy được không có nghĩa là checklist nộp bài đã đủ. Bọn mình bị nhầm giữa làm xong chức năng và có đủ thứ để chứng minh là đã làm xong."* — `P2` (Học viên L3A, phỏng vấn)
11. *"Đừng tự nghĩ ra yêu cầu nếu file không có. Cứ nói không thấy trong tài liệu để mình hỏi coach còn hơn là trả lời chắc chắn mà sai."* — `P2` (Học viên L3A, phỏng vấn)
12. *"AI gom ý khá ổn, nhưng có mấy ý nhỏ nằm trong đoạn ghi chú thì mình vẫn phải tìm lại."* — `P3` (Học viên L3B, phỏng vấn)

## 4. Các nguồn có khớp nhau không

- **Khảo sát học viên (`N = 23` L3) khớp với cấu trúc dữ liệu thật của 5 repo lab:** 5 repo lab L3 K5 có từ **6 đến 23 file `.md`** mỗi repo (tổng 67 file, 453 mục — `data/DATA_CARD.md`), khớp trực tiếp với phản ánh của học viên: **56,5% (13/23)** mở ≥4 file/buổi, **52,2% (12/23)** câu 9 phàn nàn hướng dẫn phân tán hoặc quá dài, và **52,2% (12/23)** từng gặp hai file ghi khác nhau.
- **Khớp với góc nhìn bước đầu từ Lab coach (`S06`, n = 1):** coach xác nhận nhận 11–20 câu hỏi/ca đã có đáp án trong tài liệu (mất 10–30 phút/ca).
- **Phỏng vấn (3 người) khớp khảo sát ở chỗ đau:** 3/3 mở nhiều file `.md` dẫn chiếu nhau (P1 4–5 tab, P2 ~5 file, P3 4–6 file) — khớp 13/23 mở ≥4 file và nhãn `phan_tan` ở câu 9; 3/3 kể nhóm từng làm thiếu / suýt nộp thiếu — khớp 16/23 từng làm thiếu / sai.
- **Phỏng vấn giải thích điều khảo sát chưa trả lời được:** vì sao 20/23 đã dán hướng dẫn vào AI chung mà vẫn 16/23 từng làm thiếu / sai. 2/3 (P2, P3) kể AI tóm tắt bỏ sót điều kiện phụ nằm cuối mục hoặc trong ghi chú, nên cả hai đã tự bắt AI ghi file nguồn rồi mở file kiểm lại. Cả 3 lần thiếu đều cùng một kiểu: chỉ đọc CHECKPOINTS, phần phải nộp kèm (kết quả kiểm thử, minh chứng) nằm ở SUBMISSION / RUBRIC / GUIDE.
- **Chỗ lệch:** P1 không nhớ lần nào AI trả lời sai, nhưng cũng nói "lười đọc lại kiểm chứng lại" — nên chưa rõ AI đúng thật hay lỗi không bị phát hiện. Ghi chép P3 có hai mức thời gian khác nhau (xem bảng §2), nên nhóm không dùng số phút của P3 cho bảng impact.

## 5. Kết luận

- Giả thuyết ở `evidence/hypothesis.md`: **ĐÚNG** — cả hai điều kiện xác nhận đều vượt ngưỡng trên đúng đối tượng học viên L3 ngoài nhóm (`N = 23 ≥ 20`): **60,9% (14/23)** mất ≥15 phút/lab chỉ để tìm yêu cầu (ngưỡng ≥50%) và **69,6% (16/23)** từng làm thiếu/sai yêu cầu ≥1 lần (ngưỡng ≥30%).
- **Điều vẫn chưa biết / giới hạn:** (1) Mẫu khảo sát là mẫu tự chọn, có thể nghiêng về người từng gặp khó; (2) Phỏng vấn chỉ có 3 người, cùng vai học viên, P1 đã điền khảo sát nên không độc lập hoàn toàn; chưa phỏng vấn lab coach (chỉ có 1 phản hồi khảo sát); (3) Phần pain "đọc không hiểu nội dung kỹ thuật" (6/23 ở câu 9) nằm ngoài lát cắt tra-và-trích yêu cầu nộp.

## Lịch hẹn phỏng vấn (chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| P1 · học viên L3A, tại lớp | 27/11, khoảng 19:30–19:40 | ☑ |
| P2 · học viên L3A, tại lớp | 27/11, khoảng 19:35–19:45 | ☑ |
| P3 · học viên L3B, tại phòng trọ | 27/11, khoảng 22:00–22:15 | ☑ |
