# Chi phí khi dùng thật

> Điền ở guide bước 4.2, nộp ở CP4 14:30 Thứ Bảy 28/11. Ôn lại: ngày 13, ngày 1, ngày 14 · lab ngày 13, lab ngày 14. Chấm ở rubric R6.
> Số **không điền tay**: điền `cost/personas.yaml` → `python run.py simulate` → chép bảng trong `cost/simulate-N-summary.md` vào đây.
> Lúc build dùng gói miễn phí vẫn tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`), một phiên = một buổi lab:

  | Kiểu | Tỉ lệ | Phiên / người / tháng | Lượt hỏi / phiên | Lượt / tháng |
  |---|---:|---:|---:|---:|
  | dùng ít | 0,3 | 9 | 2 | 18 |
  | dùng vừa | 0,5 | 12 | 4 | 48 |
  | dùng nhiều | 0,2 | 12 | 8 | 96 |

  Nguồn: số lượt / tháng theo `spec.md` §2 *(tự ước tính theo 12 buổi lab / tháng)*; cách tách phiên × lượt và **tỉ lệ mỗi kiểu: (tự ước tính)**.
- **Số người dùng thật** 3 kịch bản: thấp 300 *(tự ước tính)* · cơ sở 700 · cao 1.000. Nguồn cơ sở và cao: `02-guide.md` mục 4.2 của repo đề (lớp L3 hơn 700 học viên, cả khoá hơn 1.000).
- **Giá** (USD / 1 triệu token, standard; `further-reading/model-prices.md`, BTC tra 25/11/2026, https://developers.openai.com/api/docs/pricing): `gpt-4o-mini` vào 0,15 · ra 0,60 — `gpt-5.4-mini` vào 0,75 · ra 4,50.
- **Tỉ lệ đạt** dùng để tính: **18/26 (69%)** — lượt `run-5@20261128-105400` (là lượt 2).
- **Đo token trên `gpt-4o-mini`, tính giá `gpt-4o-mini` và `gpt-5.4-mini`.** `gpt-5.4-mini` chưa chạy bộ câu thử: chi phí / task thành công của nó **giả định cùng tỉ lệ đạt (tự ước tính)**.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-115208` · 50 phiên · seed 42 · 0 phiên lỗi · trace `traces/simulate-1.jsonl`

| Kiểu | Số phiên mô phỏng | Lượt / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dùng ít | 11 | 2 | 9.811 | 230 | 2,2 | 6,5 |
| dùng vừa | 20 | 4 | 19.021 | 482 | 4,4 | 13,6 |
| dùng nhiều | 19 | 8 | 37.557 | 897 | 9,1 | 27,0 |

| Model | Chi phí / phiên | Chi phí / task thành công | / tháng — thấp (300) | / tháng — cơ sở (700) | / tháng — cao (1.000) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|
| `gpt-4o-mini` (đang dùng) | $0,0040 | **$0,0057** | $11,40 | **$26,61** | $38,01 | $0,0380 |
| `gpt-5.4-mini` | $0,0207 | $0,0298 | $59,57 | $138,99 | $198,56 | $0,1986 |

Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt — **không coi như đạt 100%**.

**Đọc bảng cho đúng:**
- Tỉ lệ đạt được đo **theo từng câu thử**, còn một phiên có trung bình 5,1 lượt hỏi. Chi phí / câu hỏi đạt: $0,0011 (`gpt-4o-mini`) · $0,0059 (`gpt-5.4-mini`).
- "Chi phí / phiên" là trung bình trên 50 phiên mô phỏng, trong đó kiểu dùng nhiều ra 19/50 (cao hơn tỉ lệ 0,2 đã khai). Chi phí / tháng được tính theo tỉ lệ đã khai, nên không bị lệch vì điều này.
- Mỗi lượt hỏi lấy ngẫu nhiên một câu `thuong` / `kho` trong bộ thử và chạy độc lập (không dùng phần nhớ lab trong phiên). Câu hỏi thật có thể dài, ngắn khác đi.

## 3. So với impact

- Impact / người / tháng (`spec.md` §2): 12 lần × 23,5 phút = **282 phút (~4,7 giờ)** mỗi học viên mỗi tháng *(tự ước tính từ khảo sát)*. Đây là **thời gian đang mất**, chưa phải thời gian đã tiết kiệm được.
- Chi phí / người / tháng (cơ sở, `gpt-4o-mini`): **$0,038** · `gpt-5.4-mini`: $0,199.
- **Kết luận một dòng — đáng làm không:** chi phí model không phải rào cản (khoảng $27 / tháng cho 700 người với `gpt-4o-mini`), nhưng chất lượng 69% **chưa đạt chuẩn 80%** và chưa đo được thời gian tiết kiệm thật, nên **tiếp tục cải tiến (iterate)**, chưa đưa vào dùng.

## 4. Độ nhạy và chi phí chưa tính

- **Đổi model:** cùng số token, `gpt-5.4-mini` đắt khoảng 5,2 lần `gpt-4o-mini`; chỉ đáng đổi nếu đo được tỉ lệ đạt cao hơn trên cùng bộ câu thử.
- **Cắt ngữ cảnh:** token vào chiếm phần lớn. Lượt 2 đưa nhiều mục hơn cho model nên token vào trung bình tăng 3.828 → 4.782 / câu (+25%, `run-1` so với `run-5`).
- **Chưa tính:** máy chủ, lưu trữ, cập nhật tài liệu lab, giờ lab coach xử lý câu được chuyển sang.
- Chi phí chạy chính mô phỏng này: khoảng $0,20 (1.201.937 token vào, 29.204 token ra, giá `gpt-4o-mini`).
