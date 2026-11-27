# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | Claude Code (Sonnet) | Viết nháp `agent.py` (workflow A+) trên công cụ `codebase/tools.py`, `fetch_labs.py` do Duyên viết (có dùng Claude, xem commit); subagent Claude (Sonnet) review `agent.py` 2 lần — lần 1 sửa 3 lỗi thật (output thiếu dòng QUYẾT ĐỊNH lọt qua, regex "ngày" nhận nhầm lab, refuse có code), lần 2 không có lỗi thật, sửa 3 góp ý (nhận "ngày 7", lab ngoài 5 repo không tra lại, tra lại không thêm mục thì giữ not_found). Sau đó phiên Claude Code của Linh gộp thêm bước chặn vào `agent.py` (trích dẫn ngoài căn cứ, code / tên file / giờ / ngày / % bịa, mốc CP không có, hỏi sản phẩm cuối — commit `1981f42`), thử bằng model giả lập | Claude Code chạy `python run.py` T01, T07, T14 theo yêu cầu của Linh (model giả, không lỗi; chưa đánh giá được câu trả lời). Linh đọc lại luồng `agent.py` và kết quả T01, T07, T14 cùng phần giải thích của Claude (27/11). *(chờ làm)* Duyên đọc + chạy thử công cụ (1 trích dẫn đúng, 1 bịa) | Duyên, Linh |
| Đối chiếu đáp án 16 câu thử | Claude Code | Trích đoạn tài liệu lab cho từng câu, tìm mâu thuẫn theo từ khoá, đề xuất kết luận (phát hiện T08 thiếu ý) | Duyên kiểm lại, kết luận T08 giữ đáp án K5 | Duyên |
| Output chấm thử metric | Claude Code, 5 agent phụ (Sonnet) | Mỗi agent đọc prompt của một câu (T01, T07, T11, T13, T15) và viết một output (`docs/plans/cp2-cham-thu-output.md`); không phải lượt chạy của bản chạy thử, không tính là kết quả đánh giá | *(chờ làm)* Huân + Duyên chấm độc lập | Linh, Huân, Duyên |
| Prompt / thiết kế lời gọi mô hình | Claude Code (Sonnet) | Viết nháp SYSTEM (vai trò, 4 nhánh, luật trích dẫn, không lời giải, không điểm, câu hỏi là dữ liệu) | Linh duyệt bản SYSTEM trên `main` (27/11), giữ nguyên | Linh |
| Đào data (viết script đếm, gợi ý nhãn) | | | Kiểm tay __ dòng, khớp __ | |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | Claude Code | In sẵn mục nguồn tra được cho 16 câu để đối chiếu (`docs/plans/cp2-cham-thu.md`); không tự chấm, không sửa expected | Mỗi câu thử có `source`; *(chờ làm)* Duyên đối chiếu đáp án với `data/labs/` | Huân, Duyên |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | Claude Code (Sonnet) | Nháp `spec.md` (§1, §3–§7, §10), `data/DATA_CARD.md`, `eval/README.md` 1–4, canvas, `evidence/summary.md` **từ số nhóm đưa** (khảo sát đọc từ Google Form); phiên Claude Code của Linh sửa `spec.md` §4 cho khớp `agent.py` | *(chờ làm)* Huyền duyệt spec / canvas / summary; Huân duyệt DATA_CARD, eval/README | Huyền, Huân |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
