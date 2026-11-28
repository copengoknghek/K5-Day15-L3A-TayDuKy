# Tóm tắt mô phỏng simulate-1@20261128-115208

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| dung_it | 11 | 2 | 9811 | 230 | 2.2 | 6.5 |
| dung_vua | 20 | 4 | 19021 | 482 | 4.4 | 13.6 |
| dung_nhieu | 19 | 8 | 37557 | 897 | 9.1 | 27.0 |

Tỉ lệ đạt dùng để tính: 18/26 (69%) — lượt run-5@20261128-105400

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-5.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (300 người) | Chi phí / tháng — cơ sở (700 người) | Chi phí / tháng — cao (1.000 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gpt-4o-mini (vào 0.15 · ra 0.6 $/1M) | $0.0040 | $0.0057 | $0.0011 | $11.40 | $26.61 | $38.01 | $0.0380 |
| gpt-5.4-mini (vào 0.75 · ra 4.5 $/1M) | $0.0207 | $0.0298 | $0.0059 | $59.57 | $138.99 | $198.56 | $0.1986 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (5.1) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gpt-4o-mini. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 0/50.
