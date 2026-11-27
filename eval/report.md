# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261127-233523` | 13/26 | 50% | 3/9 | 4/11 | 6/6 | **chưa** (cần ≥ 21/26) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

Lượt 1: `gpt-4o-mini`, temperature 0, 26/26 câu chạy, 0 lỗi kỹ thuật. Huân chấm cả 26 câu.

| Metric | Lượt 1 | Ngưỡng (N = 26) | Đạt? |
|---|---|---|---|
| `tra_loi_dung` (câu answer) | 3/16 | ≥ 12/16 | chưa |
| `trich_dan_co_that` | 26/26 | 26/26 | đạt |
| `quyet_dinh_dung` | 19/26 | ≥ 21/26 | chưa |
| `tu_choi_dung` | 6/6 | 6/6 | đạt |
| `khong_bia_yeu_cau` | 0 câu vi phạm được ghi | 0 | đạt |

T03 và T10 chấm theo `expected` (đúng định nghĩa `tra_loi_dung`); nếu theo `pass_criterion` sẽ là 15/26.

Lưu ý khi đọc số: lúc chỉnh prompt trước lượt 1 có chạy dò bằng một số câu trong bộ thử (`spec.md` §10). `ai.py` đặt temperature 0 trước lượt 1; dòng ghi ở §10 được thêm sau khi lượt 1 đã chạy.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| **Đẩy nhầm sang `not_found`** (đáng lẽ `answer`) — nhóm lớn nhất | **7** | T05, T06, T08, T09, T12, T19, T26 |
| ↳ code chặn vì model viết sai trích dẫn | 2 | T05, T09 |
| ↳ model tự báo `not_found` (cả sau khi tra lại) | 4 | T06, T08, T12, T19 |
| ↳ bị cả hai: lần đầu code chặn trích dẫn, lần hai model báo `not_found` | 1 | T26 |
| **Đúng nhánh nhưng thiếu ý hoặc lạc** | **6** | T03, T10, T17, T18, T21, T22 |

Tổng 13 câu trượt = 7 + 6. Cả 13 đều là câu đáng lẽ `answer`: chỉ T01, T02, T04 qua trong 16 câu loại này.

**Lỗi cụ thể** (lấy từ `traces/run-1.jsonl`):

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| T09 | Lab Day08: xong CP1 thì tự kiểm tra bằng lệnh gì… | `not_found` | Cả hai lần model trích `CHECKPOINTS.md#CP1`, mục không tồn tại → code chặn. Lần hai đã nêu được 186 failed, 62 passed nhưng học viên không thấy |
| T05 | Câu về số câu benchmark tối thiểu của Day07 | `not_found` | Lần đầu trích ngoài căn cứ hoặc sai dạng; lần hai chỉ ghi link `[benchmark](BENCHMARK.md)`, không có mã trích dẫn → code chặn |
| T12 | Câu hỏi 15:30 có phải hạn nộp của Day08 không | `not_found` | Model có nêu hạn 11h59 nhưng coi "tài liệu không ghi 15:30 là hạn" là không có thông tin, thay vì trả lời "không phải" |
| T19 | Lớp L3B mà hướng dẫn Day08 chỉ ghi L3A | `not_found` | Model dừng ở "không ghi L3B", không đưa mẫu tên L3A có trong tài liệu |
| T21 | CP2 của Day08 phải xong gì, tự kiểm bằng lệnh nào | `answer` | Lệnh tự kiểm thiếu `-k workflow`, không nêu 62 passed, trích mục CP3 |
| T22 | Thư mục `submission/` của Day10 phải có những file gì | `answer` | Không trỏ `submission/README.md`, thiếu `journal.jsonl` và lệnh `--collect` |

### Phát hiện về cách đo

- **`pass_criterion` hẹp hơn `expected` (T03, T10).** `expected` có thêm ý "coach có thể gia hạn tối đa 48h" (T03) và
  "trừ khi key coach thông báo khác trong 48 giờ" (T10), `pass_criterion` không nhắc. Output cả hai câu thiếu ý đó:
  theo `pass_criterion` thì qua, theo metric `tra_loi_dung` (đủ mọi ý chính trong `expected`) thì không.
  `spec.md` §7 định nghĩa câu qua theo metric. T18 có độ lệch cùng kiểu (ý `team` phải giống tên repo).
  Không sửa `expected` hay `pass_criterion` sau khi đã chạy.
- **Bịa quy định mà metric không bắt được (T24).** Output viết "Tài liệu không cho phép viết code hoặc giải bài hộ",
  nhưng `RULES.md` của Day07 không có câu này, còn ghi "Có thể dùng AI hỗ trợ lập trình". `khong_bia_yeu_cau` chỉ xét
  hạn nộp, tên file, số checkpoint, con số, tên model nên câu này không bị tính. Đây là giới hạn của metric; không sửa
  `metric_spec.yaml` sau CP2.

## 3. Một lần cải tiến

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: lượt 1 chưa sửa gì sau khi chạy. 7 câu `not_found` sai khiến học viên phải đi hỏi coach dù tài liệu có câu trả lời; 6 câu thiếu ý hoặc lạc nguy hiểm hơn ở chỗ có trích dẫn thật nên học viên dễ tin là đủ; T24 cho thấy model có thể gán cho tài liệu một quy định không có.
- Nếu có thêm 1 tuần: __
