# Khảo sát — phân tích lần 1 (bản tóm tắt Google Form)

- Form: "Khảo sát nhanh (3 phút): đọc hướng dẫn khi làm lab trên lớp"
- Đọc lúc: ~17:45 Thứ Sáu 27/11/2026, từ trang **Bản tóm tắt** của form (không phải từng dòng)
- Tổng: **23 câu trả lời** — câu 1 (vai): L3A 20 · L3B 1 · L2 1 · lab coach/TA 1. Câu 2–10: **n = 22** (lab coach đi nhánh C1–C3)
- **Giới hạn:** (1) n = 22 còn gồm 1 học viên L2, chưa lọc được vì bản tóm tắt không tách theo vai → cần xuất Sheet để lọc đúng học viên L3. (2) **Chưa biết thành viên nhóm có điền không** — nếu có, phải loại (người trong nhóm không tính là bằng chứng). Sau khi loại, số học viên L3 ngoài nhóm phải còn **≥20** mới đạt ngưỡng. (3) Mẫu tự chọn (người thấy tin nhắn và chịu điền), nghiêng về người đã gặp khó.

## 1. Đối chiếu giả thuyết (`evidence/hypothesis.md`)

| Giả thuyết | Đếm | Kết quả |
|---|---|---|
| ≥50% mất **≥15 phút** mỗi lab chỉ để tìm yêu cầu (câu 4) | 15–30' 9 + 30–60' 3 + >60' 1 = **13/22 (59,1%)** | ✅ đạt |
| ≥30% từng làm **thiếu / sai** yêu cầu ≥1 lần (câu 6) | 1 lần 4 + 2–3 lần 8 + >3 lần 2 = **14/22 (63,6%)** | ✅ đạt |

→ Hai vế đều đạt (giả thuyết chỉ cần một). Kết luận tạm: **giả thuyết đúng**, chờ lọc L3 ngoài nhóm.

## 2. Số chính

| Câu | Chỉ số | x/N | % |
|---|---|---|---|
| 2 | Làm lab trong tuần này (chuyện gần đây) | 22/22 | 100% |
| 3 | Mở **≥4 file** hướng dẫn ở lab gần nhất | 14/22 | 63,6% |
| 3 | Mở **≥6 file** | 8/22 | 36,4% |
| 4 | Mất ≥15 phút chỉ để tìm yêu cầu | 13/22 | 59,1% |
| 4 | Mất ≥30 phút | 4/22 | 18,2% |
| 5 | **Dán hướng dẫn vào ChatGPT/Claude/Gemini** khi chưa chắc | 20/22 | 90,9% |
| 5 | Đọc lại / tìm trong file | 15/22 | 68,2% |
| 5 | Hỏi bạn cùng nhóm | 10/22 | 45,5% |
| 5 | Hỏi lab coach / TA | 5/22 | 22,7% |
| 5 | Đoán rồi làm tiếp | 3/22 | 13,6% |
| 6 | Từng thiếu / sai yêu cầu ≥1 lần | 14/22 | 63,6% |
| 6 | Từng thiếu / sai ≥2 lần | 10/22 | 45,5% |
| 8 | **Từng thấy hai file ghi khác nhau** về cùng một việc | 13/22 | 59,1% |
| 10 | Đã thử nhờ AI tóm tắt hướng dẫn (trong số người trả lời câu 10) | 12/14 | 85,7% |
| 11 | Sẵn lòng cho phỏng vấn thêm | 1/7 người trả lời câu 11 | — |

Lab coach (C1–C3, **n = 1**, chỉ là gợi ý, không phải bằng chứng): 11–20 câu hỏi / ca mà đáp án đã có trong file, mất 10–30 phút.

## 3. Câu 9 — điều khó chịu nhất (gắn nhãn, n = 22)

Nhãn (một câu trả lời có thể có >1 nhãn):
- **phan_tan** — phải đi qua nhiều file, file dẫn chiếu nhau, thông tin chồng chéo
- **dai** — dài, nhiều chữ
- **kho_hieu** — đọc không hiểu, không rõ
- **mau_thuan** — hướng dẫn khác nhau giữa các nguồn
- **thieu_chi_tiet** · **khong_co** · **khac**

| Nhãn | x/22 | % |
|---|---|---|
| phan_tan | 7 | 31,8% |
| dai | 7 | 31,8% |
| phan_tan **hoặc** dai | 11 | 50,0% |
| kho_hieu | 6 | 27,3% |
| mau_thuan | 1 | 4,5% |
| thieu_chi_tiet | 1 | 4,5% |
| khong_co | 2 | 9,1% |
| khac ("Đọc file readme") | 1 | 4,5% |

Nhãn do một người gắn → **cần người thứ hai gắn lại độc lập** cho kiểm lại được.

## 4. Trích dẫn nguyên văn (bỏ tên, ≤2 câu)

1. "Các file cứ dẫn chiếu đến nhau, ở file này thì lại hướng dẫn cụ thể ở một file khác" — câu 9
2. "Hướng dẫn dài và tốn kha khá thời gian để hiểu, cộng với việc chạy song song với thời gian Checkpoint nên bị chậm tiến độ" — câu 9
3. "Sai cách đặt tên repo giữa Lms và repo, bên cạnh đó hướng dẫn sai với lab coach nói" — câu 9
4. "Ghi sai tên repo" — câu 7
5. "Sai chỗ link nộp bài hôm lab 1 do làm mini lab" — câu 7
6. "Nếu tôi làm nhanh để kịp tiến độ thì coi như là cho AI làm hết, bản thân chỉ đọc hiểu, không được thực hành" — câu 10
7. "cái này làm sao vậy, ủa mở cái này sao chạy sao" — C3 (lab coach kể lại câu hỏi nhận được)

## 5. Ý nghĩa cho thiết kế

- **Cách đang làm là dán vào AI chung (20/22).** Đây là đối thủ chính ở `spec.md` §3. Câu 10 cho thấy chỗ hỏng: AI chung làm hộ luôn, học viên không còn được thực hành. Điểm khác của nhóm phải chứng minh bằng số: trích đúng `file#mục`, không bịa, không đưa lời giải.
- **Tài liệu mâu thuẫn là chuyện thật (13/22).** Câu thử kiểu T08 (K4/K5) đáng giữ; nên thêm câu `kho` loại này.
- **"Khó hiểu" (6/22) là pain về nội dung,** lát cắt tra-và-trích không giải quyết trực tiếp. Ghi vào "Không làm" hoặc "Điều vẫn chưa biết".
- **Lỗi nộp sai có thật:** tên repo, link nộp, email trong file report (câu 7) → nguồn câu thử `nguoi_dung` cho CP3.
- **Phỏng vấn khó hẹn (1/7 đồng ý)** → cần đổi cách tìm người (hỏi trực tiếp tại lớp, nhờ lab coach).

## 6. Việc cần làm tiếp

1. Xuất Sheet (bỏ cột liên hệ) → lọc **học viên L3, ngoài nhóm** → tính lại mọi số với N mới. Lưu bản ẩn danh `evidence/survey/responses-anon.csv`; bản gốc đặt tên `raw-*` (đã gitignore).
2. Nếu sau khi lọc N < 20 → xin thêm phản hồi trước CP3.
3. Người thứ hai gắn nhãn lại câu 9.
4. Câu 7, 9, C3 → viết lại thành câu thử `nguoi_dung: khảo sát câu …` cho CP3.
