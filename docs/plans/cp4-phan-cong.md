# Phân công CP4 — TayDuKy · hạn 14:30 Thứ Bảy 28/11 · 4 điểm

> Nguồn: repo đề (commit `b568b95`): README → CP4 · `02-guide.md` 4.1–5.3 · `03-rubric.md` R5, R6, R7, Bonus.
> Hiện trạng đọc từ repo lúc ~09:40 ngày 28/11. **Giờ là đề xuất.** Muộn hoặc thiếu → 0 điểm mốc.
> **Đích của nhóm: nộp xong lúc 14:00** (14:00 vào phòng demo).

## 1. CP4 phải có gì

| # | Phải có | Hiện trạng | Phụ trách chính |
|---|---|---|---|
| 1 | Phòng demo + link repo | Phòng H210 · Zone 1 (`spec.md` tiêu đề) | Huyền |
| 2 | Đủ 7 hạng mục bắt buộc | Thiếu mô phỏng chi phí, slide | cả nhóm |
| 3 | Kết quả lượt 1 → lượt 2 | Lượt 1: 13/26. Chưa có lượt 2 | Linh sửa · Duyên chạy · Huân chấm |
| 4 | Chi phí / task thành công (kịch bản cơ sở) + tên model | `cost/` còn mẫu | Linh |
| 5 | `demo-slides.pdf` ở thư mục gốc | Chưa có | Huyền |
| 6 | Link video demo dự phòng | Có video 30 giây của CP3; **quay lại sau khi khoá code** (mục 4.4) | Huyền · Duyên |
| 7 | Phần chưa xong (nếu có) | — | Huyền |
| + | *Bonus +5:* `validation/log.md`, ≥2 người ngoài nhóm | Chưa có | Huân |

## 2. Ai sửa file nào

| File / mục | Người sửa |
|---|---|
| `codebase/agent.py` | **Linh** |
| `codebase/tools.py`, `ai.py`, web (`web.py`, `static/`, `render.yaml`, `docs/deploy.md`) | **Duyên** |
| `cost/personas.yaml`, `cost/cost-estimate.md`, `spec.md` §8 | **Linh** |
| `spec.md` §10, `docs/ai-usage.md` | **Linh** (người khác nhắn dòng cho Linh) |
| `README.md` | **Duyên** |
| `spec.md` §9 | **Huyền** |
| `spec.md` §7 dòng "Kết quả", `eval/report.md`, `eval/README.md` mục 5–6 | **Duyên** |
| `eval/run-2.csv` | Duyên tạo · **Huân** điền `pass`, `ghi_chu` |
| `validation/log.md` | **Huân** |
| `slides/outline.md`, `demo-slides.pdf` | **Huyền** |
| `reflection/<ten>.md` | mỗi người file của mình |

`spec.md` có ba người sửa trong khung 12:45–13:30 (Duyên §7, Linh §8 và §10, Huyền §9): mỗi người `git pull` **ngay trước khi sửa**, commit nhỏ và push liền.
Lúc nộp `spec.md` phải đủ §0–§9; hiện §9 còn trống.

## 3. Lịch chung

| Giờ | Cả nhóm |
|---|---|
| 10:00–10:30 | Ngồi chung đọc 13 câu trượt, **chốt một nhóm lỗi** để sửa |
| 11:45 | **Khoá code** (`codebase/`) |
| 12:45 | Có điểm lượt 2 |
| 13:30 | Slide bản cuối; đi lại câu chuyện Pain → Impact → Giải pháp → Đánh giá → Chi phí |
| 13:40–13:55 | Tập demo, mỗi người nói phần mình; mở repo và video bằng cửa sổ ẩn danh |
| **14:00** | **Nộp**, vào phòng |

### Đề xuất cải tiến (nhóm quyết lúc 10:00)

Nhóm lỗi lớn nhất: **7 câu đáng lẽ `answer` bị đẩy sang `not_found`** (T05, T06, T08, T09, T12, T19, T26).

| Nguyên nhân (theo `traces/run-1.jsonl`) | Câu | Hướng sửa chung |
|---|---|---|
| Model viết sai trích dẫn nên code chặn | T05, T09, T26 | Khi tra lại, nói rõ mã sai và nhắc chép đúng mã đã đưa; xem lại dạng link Markdown |
| Model báo `not_found` dù có căn cứ liên quan | T06, T08, T12, T19, T26 | Dặn: câu hỏi có tiền đề sai hoặc chỉ ghi một phần thì trả lời phần tài liệu có, nói rõ phần không có |

Sửa theo hướng chung, **không viết riêng cho từng câu thử**.

Nếu cả `agent.py` (Linh) và `tools.py` (Duyên) cùng sửa, vẫn tính là **một lần cải tiến** khi cùng nhắm nhóm lỗi này.
Linh ghi một mục §10 cho cả hai thay đổi, **trước 11:45**.

### Web và deploy

- **Demo chạy trên máy là đủ. Không deploy** (đề xuất): đưa key lên máy chủ thì ai có link cũng dùng được bằng tiền của nhóm.
- Nếu vẫn deploy: key chỉ đặt trong biến môi trường của Render, đặt hạn mức chi tiêu, tắt sau buổi demo.
- Web phải vào `main` **trước 11:45** và không đổi luồng của `agent.py`, để lượt 2 đo đúng bản đem demo.
- `python run.py` vẫn phải chạy được.

## 4. Việc theo người

### 4.1 Vũ Gia Linh — cải tiến, mô phỏng chi phí

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 10:30–11:30 | Sửa prompt / bước chặn theo nhóm lỗi đã chốt. Thử bằng `python run.py` | `codebase/agent.py` | Có commit, đã push |
| 11:30–11:45 | Ghi thay đổi **trước khi chạy lượt 2** | `spec.md` §10, §4 | Đã push |
| 11:45–12:30 | Điền persona (≥3 kiểu), số người dùng 3 kịch bản, giá ≥2 model; bỏ hết chữ "(ví dụ)" | `cost/personas.yaml` | `python run.py simulate --try` chạy được, không còn cảnh báo "(ví dụ)" |
| 12:45–13:05 | Chạy ≥50 phiên với tỉ lệ đạt của lượt 2; commit **đủ ba file** | `cost/simulate-N.csv`, `cost/simulate-N-summary.md`, `traces/simulate-N.jsonl` | Đã push |
| 13:05–13:30 | Chép bảng, viết so với impact và một dòng kết luận | `cost/cost-estimate.md`, `spec.md` §8 | Số nào cũng truy được về file hoặc nguồn |
| 13:30 | Ghi phần dùng AI của CP4 | `docs/ai-usage.md` | Khớp việc đã làm |

```powershell
python run.py simulate --rate-from eval/run-2.csv
```

- **Chỉ Linh chạy bản đầy đủ**, vì khung tự đánh số lượt. Người khác muốn thử thì dùng `--try`.
- Persona gọi nhiều lượt thì chạy lâu; nếu bị giới hạn lượt gọi, thêm `--wait 4`.

Số đầu vào:
- `cost-estimate.md` ghi "đo token trên `gpt-4o-mini`, tính giá `gpt-4o-mini` và `gpt-5.4-mini`".
- **Chi phí / task thành công của `gpt-5.4-mini`:** khung dùng luôn tỉ lệ đạt của lượt 2 (chạy bằng `gpt-4o-mini`) cho mọi dòng giá và không cảnh báo ở từng dòng. Ghi rõ *(giả định cùng tỉ lệ đạt — tự ước tính)*, vì `gpt-5.4-mini` chưa chạy bộ câu thử.
- Số người dùng: "lớp L3 hơn 700 học viên, cả khoá hơn 1.000" trích từ `02-guide.md` mục 4.2; kịch bản thấp ghi *(tự ước tính)*.
- Số lượt hỏi / tháng đã có ở `spec.md` §2: ít ~18, vừa ~48, nhiều ~96 *(tự ước tính)*. Trong `personas.yaml` tách thành số phiên × số lượt (vd 9×2, 12×4, 12×8, *tự ước tính*); tỉ lệ mỗi kiểu cũng ghi *(tự ước tính)* nếu không có nguồn.
- Giá (USD / 1 triệu token, `further-reading/model-prices.md`, BTC tra 25/11): `gpt-4o-mini` vào 0.15, ra 0.60 · `gpt-5.4-mini` vào 0.75, ra 4.50. Ghi link https://developers.openai.com/api/docs/pricing và ngày xem 25/11/2026.
- **Dòng so với impact:** lấy từ `spec.md` §2: 12 lần × 23,5 phút = 282 phút (~4,7 giờ) / học viên / tháng, đặt cạnh chi phí / người / tháng (kịch bản cơ sở). Ghi thêm đây là thời gian đang mất, chưa phải thời gian đã tiết kiệm được.
- Chi phí chạy mô phỏng ước chừng dưới 1 USD *(tự ước tính từ token lượt 1)*.

**Phải trả lời được:** sửa gì, vì sao? Chi phí / task thành công tính thế nào? Vì sao workflow mà không phải agent?

### 4.2 Nguyễn Thị Duyên — lượt 2, báo cáo, demo

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 10:30–11:00 | Đưa web lên `main` nếu nhóm đồng ý dùng để demo | `codebase/web.py`, `static/` | `python codebase/web.py` chạy trên máy demo |
| 11:00–11:30 | Nếu lỗi nằm ở tra cứu thì sửa `tools.py`; không thì thử lại bản Linh sửa | `codebase/tools.py` | Báo Linh kết quả |
| 11:45–12:00 | `git pull`, chạy **cả bộ**, commit và push cả hai file | `eval/run-2.csv`, `traces/run-2.jsonl` | 0 lỗi; Huân nhận được |
| 12:00–12:45 | Viết sẵn mục 3, 4 của báo cáo (chờ số) | `eval/report.md` | — |
| 12:45–13:15 | Điền số lượt 2: nhóm lỗi __ → __, tổng % trước → sau, **câu nào tệ đi** | `eval/report.md`, `eval/README.md` 5–6, `spec.md` §7 | Đã push; gửi số cho Huyền |
| 12:00–12:30 | Cùng Huyền quay video demo dự phòng bằng bản đã khoá | link video | 1 câu thường + 1 câu khó |
| 13:15–13:30 | Kiểm máy demo: `.env`, `data/labs/`, hỏi thử 1 câu | — | Trả lời được |
| 13:30–13:40 | Cập nhật phần thật / giả, web (nếu có), link video | `README.md` | Khớp code, đã push |

```powershell
python run.py eval
```

```powershell
python run.py score eval/run-2.csv
```

- Lượt có lỗi kỹ thuật: không sửa tay, chạy thành lượt mới, giữ cả hai.
- Chạy lượt 2 muộn nhất 12:00, kể cả cải tiến chưa trọn.
- `eval/report.md` (R5): ≥3 lỗi, mỗi lỗi đủ input · output · vì sao sai, gom nhóm có tên; % lượt 1 → lượt 2 so với chuẩn "đạt". Câu tệ đi vẫn ghi.
- `eval/README.md` là hồ sơ một trang: dataset → bộ câu thử → metric → bảng các lượt → lỗi chính.

**Phải trả lời được:** model được nối thế nào, token lấy ở đâu? Trích dẫn bịa bị chặn ở đâu? Một câu trượt vì sao trượt?

### 4.3 Nguyễn Đức Huân — chấm lượt 2, người dùng thử

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 10:30–11:30 | Cho ≥2 **học viên L3 ngoài nhóm** dùng thử, ~10 phút / người, 5 nhịp (làm quen · bối cảnh · giao việc · quan sát · hỏi sau) | `validation/log.md` | Đủ 5 cột: vai · việc giao · quan sát · trích nguyên văn · mức nghiêm trọng |
| 11:30–11:45 | Tổng hợp 4 dòng (chủ đề lặp · sửa gì trước demo · giữ gì và vì sao · để dành sau) và dòng "rất tiếc / hơi tiếc / không sao"; báo Linh ≥1 thay đổi hoặc lý do giữ nguyên | `validation/log.md`, `spec.md` §10 (qua Linh) | Đã push |
| 12:00–12:45 | Chấm `run-2.csv` **cùng cách như lượt 1** (theo `expected`) | `eval/run-2.csv` | `score` ra % ; đã push |
| 12:45–13:00 | Chỉ cho Duyên câu tốt lên, câu tệ đi | — | — |
| 13:00–13:30 | Gửi Huyền nội dung slide 5 và 8 | — | — |

Thay đổi rút ra từ người thử mà sau 11:45 mới có thì **không vào lượt 2**: ghi §10 là "sửa trước demo" hoặc "để dành sau".

Giao việc theo kết quả, ví dụ: "dùng cái này để biết lab Day04 phải nộp gì". Người thử tự thao tác, không ghi tên.

**Phải trả lời được:** vì sao 5 metric này? Chuẩn "đạt" là gì? Vì sao 13/26?

### 4.4 Võ Thị Kim Huyền — slide, rủi ro, video, nộp

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 10:30–11:15 | §9: dữ liệu đã ẩn danh gì · AI không được làm gì · ai bị hại nếu AI sai và chặn thế nào | `spec.md` §9 | Không còn dòng trống |
| 11:15–12:45 | Slide trang 1–4, 7 (số từ `spec.md`, `evidence/`) | bản slide | Mỗi trang ≥1 số / trích dẫn có nguồn |
| 12:00–12:30 | Cùng Duyên quay video demo dự phòng bằng bản đã khoá (1 câu thường + 1 câu khó, không dùng câu tấn công); gửi link cho Duyên ghi vào README | link video | Mở được bằng cửa sổ ẩn danh, không cần đăng nhập |
| 13:15–13:30 | Ráp trang 5 (số lượt 2), 6 (chi phí), 8; xuất PDF | `demo-slides.pdf`, `slides/outline.md` | PDF ở thư mục gốc, đã push |
| 14:00 | Nộp form | — | Nộp bằng mã học viên đội trưởng |

**Phải trả lời được:** ai đau, đau thế nào, bằng chứng gì? Vì sao chọn bài này? Kết luận go / iterate / stop dựa trên số nào?

## 5. Khung 8 trang slide và người nói

| Trang | Nội dung | Số lấy từ | Người nói |
|---|---|---|---|
| 1 | Người dùng & pain | `evidence/summary.md` (N = 23) | Huyền |
| 2 | Bảng impact, hướng bị loại | `spec.md` §2 | Huyền |
| 3 | Lát cắt, sơ đồ, mức tự động | `spec.md` §4 | Linh |
| 4 | Demo live: 1 câu thường + 1 câu khó | `eval/benchmark.csv` | Duyên |
| 5 | Đánh giá: bộ câu, metric, lượt 1 → 2, lỗi chính, run ID | `eval/report.md` | Huân |
| 6 | Chi phí / task thành công, 3 kịch bản, so impact | `cost/cost-estimate.md` | Linh |
| 7 | Go / iterate / stop | trang 1, 5, 6 | Huyền |
| 8 | Nếu có thêm 1 tuần | `eval/report.md` mục 4, `validation/log.md` | Duyên |

**Demo:** giám khảo có thể đưa một câu lạ, mở trace một câu trượt, hoặc hỏi bất kỳ ai "câu này vì sao trượt?". Mỗi người chuẩn bị giải thích **một câu trượt**.

## 6. Sau CP4 → 23:59 Thứ Bảy 28/11

| Việc | Người |
|---|---|
| `reflection/<ten-khong-dau>.md`: phần mình làm (file / commit) · AI hỗ trợ thế nào · bài học từ một câu trượt | **mỗi người tự viết** |
| Sửa theo góp ý demo, ghi `spec.md` §10 | Linh |
| Chạy thêm (nếu có) thành `run-3.csv`, không dùng để chấm R5 | Duyên |
| Kiểm lần cuối: không có API key, không có dữ liệu cá nhân | Duyên + Huyền |
| Tắt web đã deploy hoặc thu hồi key (nếu đã deploy) | Duyên |

## 7. Luật dễ mất điểm

- Không sửa chuẩn "đạt", câu thử, `expected`, số bằng chứng, kết quả lượt đã chạy.
- Số trên slide phải truy được về file. Lượt 2 thấp hơn lượt 1 vẫn đủ điểm nếu ghi thật.
- Chi phí / task thành công dùng tỉ lệ đạt thật của lượt 2, không lấy 100%.
- Có API key hoặc dữ liệu cá nhân thật trong repo: trừ 10 điểm.
- Không giải thích được phần mang tên mình: phần đó 0 điểm.
