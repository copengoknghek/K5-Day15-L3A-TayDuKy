# Feedback CP2 — phần Huân duyệt · 27/11/2026

> Ghi lại để sửa sau. Mỗi dòng có người sửa và mức độ. **[GẤP]** = phải xong trước khi commit chuẩn "đạt" (hạn 19:30).
> Bối cảnh: `codebase/tools.py` và `codebase/fetch_labs.py` lấy theo bản Duyên trên `main` (PR #1, #2). Bản Claude viết trước đó đã bỏ, bản sao để ngoài repo.

## 1. `eval/metric_spec.yaml` + `spec.md` §7 (Huân + Huyền duyệt, M2)

| # | Mức | Feedback | Ai sửa |
|---|---|---|---|
| 1.1 | ✅ Đã sửa 18:5x · **[GẤP]** | `trich_dan_co_that` ghi "heading có thật", nhưng `verify_citations` của Duyên so **nguyên mã mục**. Heading trùng tên trong cùng file có mã `#<mục cha> > <heading>`. Model trích `#Deadline` thay cho `#CP4 > Deadline` thì code chấm sai, người đọc lại thấy đúng. Đề xuất sửa định nghĩa thành: "…trỏ tới một **mã mục có thật** (đúng như `search_guides` trả, kể cả phần `mục cha > heading`)…". Cả `[file.md]` không có `#mục` cũng bị code tính là trích dẫn sai; nên ghi rõ trong định nghĩa. | Huân |
| 1.2 | ✅ Đã sửa 18:5x · Nên | Ghi số câu cụ thể để chấm không phải làm tròn: 16 câu → ≥80% = **≥13/16** · 10 câu answer → ≥75% = **≥8/10** · `quyet_dinh_dung` ≥80% = **≥13/16**. | Huân |
| 1.3 | Nên | `tra_loi_dung`: "ý chính" chưa tách rõ. Ví dụ T02 có 4 file bắt buộc cộng ý "không nộp .env". Đề xuất: ý chính = các phần ngăn bởi dấu `;` hoặc `·` trong expected, **trừ** phần "trích …". | Huân |
| 1.4 | Ghi nhận | Chuẩn ≥80% và 3 điều kiện cứng khớp với quyết định D3 của nhóm. Định nghĩa "một câu qua" (D2) khớp với metric. | — |
| 1.5 | **[GẤP]** | §7 + `metric_spec.yaml` + `benchmark.csv` **chưa commit**. Sửa 1.1 xong thì commit riêng, trước 19:30. | Huân + Huyền đồng ý, Claude commit |

## 2. `data/DATA_CARD.md` + `eval/README.md` mục 1–4 (Huân duyệt)

| # | Mức | Feedback | Ai sửa |
|---|---|---|---|
| 2.1 | Đã sửa | DATA_CARD dòng "Xử lý": viết lại theo code Duyên (ghim commit, mục `(mở đầu)`, `mục cha > heading`, BM25, 2500 ký tự). Số **67 file / 453 mục / 5 hash** khớp với output `python codebase/fetch_labs.py` bản Duyên. | — |
| 2.2 | Chờ | eval/README mục 3: kết quả chấm thử x/5 còn trống, chờ chấm (xem mục 4). | Huân + Duyên |
| 2.3 | Ghi nhận | `python run.py check`: 16 câu (6/6/4), 5 metric, TEAMS hợp lệ. Còn 2 cảnh báo của CP3: cần 20–30 câu, ≥1/3 câu từ người dùng (đang 0/16). | Huân (CP3) |

## 3. Review chéo code + `spec.md` §4 (Huân chạy thử, Cặp X sửa)

| # | Mức | Feedback | Ai sửa |
|---|---|---|---|
| 3.1 | ✅ Đã sửa 18:5x · **[GẤP]** | `python run.py` **không chạy**: `ImportError: cannot import name 'normalize' from 'tools'`. Bản `agent.py` local (luồng A+, chưa commit) gọi `normalize`, `repo_for_lab`, `search_guides(..., focus_submission=True)` và `check["valid"]`, mà `tools.py` của Duyên không có những thứ đó. Cách sửa: tự nhận diện lab trong `agent.py` (regex `day|lab` + số, chỉ nhận 4/7/8/10/11) và truyền `lab=<số>` vào `search_guides`. Lần tra lại thì ghép thêm từ khoá "nộp submission checkpoint rubric deadline" vào query thay cho `focus_submission`. Chỉ dùng `ok / invalid / count` từ `verify_citations`. | Linh (luồng) + Duyên |
| 3.2 | Nên | `tools.py` (Duyên): thiếu `data/labs/` thì `_index()` ném `FileNotFoundError` và cả lượt eval lỗi. Kế hoạch ghi "báo chạy fetch_labs, không crash". Xem lại: trả `[]` kèm `note(...)`, hoặc giữ lỗi nhưng ghi rõ trong spec. | Duyên |
| 3.3 | Nên | `tools.py` vẫn còn `search_example` (ví dụ của khung). Xoá khi `agent.py` đã dùng `search_guides`. | Duyên |
| 3.4 | ✅ Đã sửa 18:5x · Nên | `spec.md` §4 viết theo bản tools cũ của Claude, cần sửa cho khớp code Duyên: bảng công cụ (bỏ `focus_submission`; "IDF" → BM25; mỗi mục ≤2500 ký tự, có dòng "Thuộc: …"; `verify_citations` không trả `valid`) · sơ đồ Mermaid bước ⑤ (`search_guides(focus_submission=True)` → "search_guides với từ khoá nộp / checkpoint") · dòng "Dữ liệu: 67 file → 453 mục" vẫn đúng. Sửa cùng lúc với 3.1. | Linh (§4) |
| 3.5 | ✅ Đã sửa 18:5x · Nên | `README.md` "Phần nào thật, phần nào giả": dòng `search_guides` ghi "IDF" → đổi thành BM25. `docs/ai-usage.md` dòng code ghi "3 lỗi review đã sửa": 2 lỗi BOM / khối code nay nằm trong code Duyên → viết lại theo thực tế. | Huyền / người viết |
| 3.6 | Ghi nhận | Mã trích dẫn kiểu `mục cha > heading` hợp lý: tách được Deadline của từng checkpoint. SYSTEM prompt trong `agent.py` nên dặn model chép **nguyên** mã (kể cả phần `>`). Hiện đã có luật "chép NGUYÊN mã trong ngoặc vuông". | Linh kiểm lại |

## 4. Việc của Huân còn chờ (không giao cho AI)

- [ ] Lịch 3 phỏng vấn (vai + giờ, không tên) → `evidence/summary.md` mục "Lịch hẹn" (đang ghi "chờ chi tiết").
- [ ] Chấm thử **độc lập** 5 output T01, T07, T11, T13, T15 khi Linh gửi. Đề + căn cứ ở `docs/plans/cp2-cham-thu.md`, phần C. Lưu ý: file này in bằng bản tools cũ (căn cứ ≤1200 ký tự). Nếu kịp, in lại bằng `search_guides` của Duyên để căn cứ giống với code thật.
- [ ] Sửa `expected` nếu Duyên đối chiếu thấy sai, trước 19:30.
- [ ] Sửa metric cùng Duyên nếu chấm thử lệch ≥2/5.
