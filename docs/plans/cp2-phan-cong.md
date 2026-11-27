# Phân công CP2 — TayDuKy · hạn 19:30 Thứ Sáu 27/11

> Kế hoạch đầy đủ: [cp2-plan.md](cp2-plan.md). Mốc M1–M9 xem mục 7 của kế hoạch.
> Session Claude (Sonnet) viết nháp code / tài liệu; **người có tên phải đọc lại, chạy thử và giải thích được phần mình** — không giải thích được thì phần đó 0 điểm.

## Lịch chung cả nhóm

| Giờ | Việc chung |
|---|---|
| **17:20–17:40** | Họp chốt D1–D5 (hình dạng, định nghĩa "đạt", chuẩn "đạt", định dạng output, số khảo sát) — **M1** |
| **18:50–19:05** | Đổi chéo review: Cặp X đọc §7 + bộ câu thử · Cặp Y chạy thử code + đọc §4 |
| **19:05–19:15** | Đi lại câu chuyện: Pain → Impact → Giải pháp → Đánh giá → Chi phí, mỗi người nói phần mình |
| Suốt buổi | Mỗi người hỏi ≥1 học viên ngoài nhóm / nhắc bạn lớp làm khảo sát |

---

## 1. Võ Thị Kim Huyền — Đội trưởng · Cặp Y (pain, câu chuyện, nộp bài)

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 17:20 | Mở Google Form: đếm **n phản hồi**, chọn **1 trích dẫn** câu 7 (bỏ tên); báo nhóm ở buổi họp | — | Có số n + 1 câu nguyên văn |
| 17:20–17:40 | Điều phối họp chốt D1–D5 | `cp2-plan.md` mục 4 tích ☐ | **M1** |
| 17:40–17:55 | Cùng Huân đọc lại §7 + `metric_spec.yaml`, đồng ý commit | `spec.md` §7 | **M2** |
| 18:00–18:30 | Canvas: dòng 4 (số + trích dẫn) · dòng "Đã đổi gì so với CP1" | `canvas.md` | Không còn ô trống |
| 18:30–19:05 | Duyệt nháp `spec.md` §1 (người dùng, pain không chữ AI) · §3 (giải pháp tương tự) · §5 (kịch bản khó) · `evidence/summary.md` (số khảo sát hiện có) | `spec.md`, `evidence/summary.md` | Số nào cũng có nguồn, không bịa |
| 19:15 | Mở repo, `spec.md`, `benchmark.csv` bằng **cửa sổ ẩn danh** | — | **M8** |
| 19:15–19:30 | **Nộp form CP2** bằng mã học viên dòng 1, nội dung lấy từ `cp2-submission.md` | — | **M9** |

**Phải trả lời được:** Ai đau, đau thế nào, bằng chứng đang có bao nhiêu? CP2 đổi gì so với CP1?

## 2. Nguyễn Đức Huân — Cặp Y (bộ câu thử, metric, data card)

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 17:20 | Chốt lịch **3 cuộc phỏng vấn** (tối nay / sáng mai), báo ở buổi họp | `evidence/summary.md` mục Lịch hẹn (vai + giờ, không tên) | 3 dòng lịch hẹn |
| 17:40–17:55 | Duyệt `metric_spec.yaml` (sửa D3b) + §7 (D2, D3) cùng Huyền → đồng ý commit | `eval/metric_spec.yaml`, `spec.md` §7 | **M2** |
| 18:00–18:20 | **Chấm thử độc lập** 5 output (T01, T07, T11, T13, T15) theo `metric_spec.yaml` — không bàn với Duyên trước khi chấm xong | Ghi chép chấm | **M4** |
| 18:20–18:50 | Duyệt nháp `data/DATA_CARD.md` (67 file, số mục, 5 hash) · `eval/README.md` mục 1–4 (lưới input, bảng metric, kết quả chấm thử x/5) | `data/DATA_CARD.md`, `eval/README.md` | `python run.py check` sạch |
| 18:50–19:05 | Review chéo: chạy `python run.py` với T01, T07, đọc §4 | — | Kể lại được luồng |

**Phải trả lời được:** Vì sao chọn 5 metric này? Một câu "đạt" nghĩa là gì? Chuẩn "đạt" bao nhiêu, vì sao?

## 3. Nguyễn Thị Duyên — Cặp X (code lõi: tài liệu lab, tra cứu, kiểm trích dẫn)

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 17:40–18:00 | Chạy `python codebase/fetch_labs.py`, kiểm số file `.md` và số mục khớp, gửi số cho Huân | `codebase/fetch_labs.py` | **M3** |
| 18:00–18:20 | **Chấm thử độc lập** 5 output cùng bộ với Huân → so kết quả, ghi x/5 | `eval/README.md` §3 | **M4** |
| 18:20–18:50 | Đọc + chạy thử `search_guides`, `verify_citations` (thử 1 trích dẫn đúng, 1 trích dẫn bịa) | `codebase/tools.py` | Giải thích được cách cắt mục và cách kiểm trích dẫn |
| 18:20–18:50 | **Đối chiếu đáp án 16 câu** với `data/labs/` (session in sẵn mục nguồn) — sai thì báo để sửa trước 19:30 | Ghi chú đối chiếu | **M6** |
| 18:50–19:05 | Review chéo: đọc §7 + bộ câu thử | — | — |

**Phải trả lời được:** AI dựa vào dữ liệu nào? Trích dẫn bịa bị chặn ở đâu, bằng gì?

## 4. Vũ Gia Linh — Cặp X (prompt, luồng, chặn rủi ro)

| Giờ | Việc | Ra file | Xong khi |
|---|---|---|---|
| 17:40–18:00 | Duyệt nháp SYSTEM prompt: vai trò · 4 nhánh · luật trích dẫn · không đưa lời giải · không trả lời điểm · câu hỏi là dữ liệu không phải lệnh · định dạng `QUYẾT ĐỊNH:` | `codebase/agent.py` (SYSTEM) | Đồng ý bản SYSTEM |
| 18:00–18:15 | Lấy **5 output** cho bộ chấm thử: dán SYSTEM + căn cứ (session in sẵn) vào ChatGPT/Claude, gửi cho Huân và Duyên | 5 output | **M4** bắt đầu được |
| 18:15–18:50 | Đọc + chạy `agent.py`: `python run.py` với T01 (thường), T07 (mơ hồ), T14 (tấn công); xem bước chặn và bước tra lại (A+) | `codebase/agent.py` | **M5** · có tóm tắt review code của subagent |
| 18:50–19:05 | Duyệt bảng công cụ + sơ đồ §4 cho khớp code | `spec.md` §4 | Sơ đồ khớp code |

**Phải trả lời được:** Vì sao chọn workflow chứ không phải agent? Lỗi nguy hiểm nhất là gì, chặn thế nào?

---

## Ai quyết những gì

| Quyết định | Người chốt |
|---|---|
| D1–D5, chuẩn "đạt" | Cả nhóm, Huyền chốt cuối |
| Đồng ý commit / push | Huyền (thay nhóm) |
| Sửa đáp án câu thử | Huân, sau khi Duyên đối chiếu |
| Sửa metric sau chấm thử | Huân + Duyên |
| Nộp form | Huyền |
