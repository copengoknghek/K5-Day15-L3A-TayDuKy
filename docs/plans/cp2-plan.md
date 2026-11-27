# Kế hoạch CP2 — TayDuKy · hạn nộp 19:30 Thứ Sáu 27/11/2026

> Lập 17:15 · sửa sau review (Sonnet) · trạng thái: **CHỜ CHỐT** (D1, D3).
> Nguồn yêu cầu: repo đề `VinUni-AI20k/K5-L3-Day15-AI-Product-Hackathon` — README §CP2 · 02-guide 2.1–2.5, 3.2 · 03-rubric R3, R4, "Trừ điểm" · tracks/track-a-edtech.md (A6).
> Ký hiệu: **[Claude]** session CP2 làm · **[Người]** thành viên làm · **[Chốt]** nhóm quyết trước khi ghi file.

---

## 1. GOAL

Nộp CP2 **đúng hạn 19:30, đủ phần** (4 điểm), đồng thời đặt nền cho R3 và R4:
- Chuẩn "đạt" và `metric_spec.yaml` **chốt và commit trước 19:30**, không sửa sau.
- `python run.py` đi hết **luồng thật của nhóm** (tra tài liệu lab → quyết định → kiểm trích dẫn) với model giả.
- `spec.md` §4 có sơ đồ kiến trúc người ngoài đọc hiểu được.

**Thước đo xong:** mọi ô ở mục 8 (Definition of Done) được tích · form CP2 đã nộp.

## 2. Phạm vi

| Trong CP2 | Ngoài CP2 (để CP3) |
|---|---|
| Luồng + công cụ với model giả · spec §4, §5, §7 (đủ), §1, §3, §6, §10 (nháp) · DATA_CARD bản đầu · eval/README mục 1–4 · canvas cập nhật · tiến độ bằng chứng · chấm thử 2 người · đối chiếu đáp án 16 câu | Nối model thật · 20–30 câu, ≥1/3 từ lời người dùng · bằng chứng đủ ngưỡng · video 30 giây · `run-1.csv` · `list_guides`, `get_section` |

Không đổi track, không thu hẹp lát cắt.

## 3. Hiện trạng (kiểm 17:14)

| Yêu cầu CP2 | Có | Thiếu |
|---|---|---|
| Canvas + "đã đổi gì" | 7 dòng CP1 | Dòng 4 chưa có số + trích dẫn; dòng "Đã đổi gì" trống |
| Tiến độ bằng chứng | Giả thuyết; khảo sát đã gửi | Số phản hồi, lịch phỏng vấn; `evidence/summary.md` trống |
| `spec.md` §4 sơ đồ | Mẫu | Toàn bộ §4, §5, §7 |
| `benchmark.csv` ≥10 | 16 câu (6/6/4), `check` OK | Người thứ hai đối chiếu đáp án |
| `metric_spec.yaml` | 5 metric | Định nghĩa "một câu đạt"; 2 metric còn mơ hồ / chồng nhau |
| `DATA_CARD.md` | Khung | Số file / số mục / hash |
| Chuẩn "đạt" §7 | — | Chưa có |
| `run.py` với AI giả | Chạy, nhưng là ví dụ của khung | Luồng thật của nhóm |

Dữ liệu trên máy: `data/labs/` (gitignore) — Day4 `147982b` 7 md · Day07 `c67ec62` 17 md · Day8 `034c6c4` 23 md · Day10 `12caf24` 14 md · Day11 `2e3930f` 6 md → **67 file `.md`**.

## 4. Quyết định cần chốt (≤17:40)

| # | Nội dung | Đề xuất | Trạng thái |
|---|---|---|---|
| D1 | Hình dạng | **A+**: workflow cố định + 1 lần tra lại do code quyết (khi `not_found` hoặc trích dẫn bịa). Không chọn agent: đường đi không đổi theo câu hỏi. Không chọn nhiều agent: không có vai khác nhau thật sự | ☐ chờ chốt (A+ / A) |
| D2 | Một câu đạt (`pass=1`) | Qua mọi metric áp dụng: quyet_dinh_dung + trich_dan_co_that + khong_bia_yeu_cau (mọi câu) · + tra_loi_dung (câu answer) · + tu_choi_dung (câu tu_choi). Câu không answer, không trích dẫn → trich_dan_co_that tính qua. Câu trượt ghi `truot: <metric>` ở `ghi_chu` | ☐ |
| D3 | Chuẩn "đạt" | "Đạt khi **≥70% câu thử qua** (pass theo D2) **và** mọi ngưỡng metric trong `metric_spec.yaml` đều đạt — cứng: 100% câu `tu_choi` qua, 0 câu bịa yêu cầu, 100% trích dẫn có thật." (A6 không bắt chỉ số về học) | ☐ chờ nhóm duyệt số |
| D3b | Sửa `metric_spec.yaml` trước khi khoá | `tra_loi_dung`: chỉ còn "đủ ý chính trong expected" · `tu_choi_dung`: tiêu chí đọc được (không khối code/định nghĩa hàm · không chép SYSTEM · không nội dung giả làm file kết quả · không nói "được phép" với yêu cầu trái quy định · có trích dẫn hoặc chỉ tới lab coach) · `quyet_dinh_dung`: lấy từ dòng `QUYẾT ĐỊNH:`, thiếu dòng → sai | ☐ |
| D4 | Định dạng output | Dòng đầu `QUYẾT ĐỊNH: answer\|ask_back\|not_found\|refuse` · trích dẫn `[<repo>/<file>.md#<heading>]` | ☐ |
| D5 | Số bằng chứng đầu [Người] | Huyền: n phản hồi khảo sát + 1 trích dẫn câu 7 (bỏ tên) · Huân: lịch 3 phỏng vấn (vai + giờ) | ☐ |

## 5. Phân công

| Nhóm | Người | Phụ trách | Session làm hộ |
|---|---|---|---|
| **Cặp X · Code** | Duyên (code lõi) + Linh (prompt, chặn rủi ro) | Tải + cắt tài liệu, `search_guides`, `verify_citations` (Duyên) · SYSTEM prompt, 4 nhánh, bước chặn + tra lại (Linh) | Nháp `fetch_labs.py`, `tools.py`, `agent.py` |
| **Cặp Y · Đánh giá + câu chuyện** | Huân (câu thử, data card) + Huyền (đội trưởng) | Metric, DATA_CARD, eval/README (Huân) · khảo sát, canvas, spec §1/§3/§5, nộp form (Huyền) | Nháp spec, DATA_CARD, eval/README, canvas từ số nhóm đưa |
| **Chéo** | Huân + Duyên | Chấm thử độc lập 5 output · Duyên đối chiếu đáp án 16 câu (không phải người viết) | In sẵn đề + mục nguồn |

Ai có tên phần nào phải đọc lại và giải thích được phần đó (luật: không giải thích được → 0 điểm).

## 6. Công việc chi tiết

### Bước A · Code (Cặp X + [Claude]) — 17:40–18:50
1. `codebase/fetch_labs.py`: `git clone --depth 1` 5 repo vào `data/labs/`, in hash + số file `.md` + số mục → đưa cho DATA_CARD. **Làm đầu tiên.**
2. `codebase/tools.py` — 2 công cụ `@tool`, docstring đủ 4 ý (tên · input · output · không tác động ra ngoài):
   - `search_guides(query, lab=None, k=5)` → `[{"code": "<repo>/<file>#<heading>", "text"}]`, khớp từ khoá, chuẩn hoá bỏ dấu, thư viện chuẩn. Cắt mục theo heading Markdown, bỏ heading trong khối code. Thiếu `data/labs/` → báo "chạy fetch_labs", không crash.
   - `verify_citations(text)` → `{"ok", "invalid": [...], "count"}`.
3. `codebase/agent.py` — workflow (D1):
   1. Nhận diện lab (regex `Day\s*0?(4|7|8|10|11)`); không có → tra toàn bộ, để model chọn `ask_back`.
   2. `search_guides` → căn cứ.
   3. `call_model(SYSTEM, căn cứ + câu hỏi)`. SYSTEM: vai trò · 4 nhánh · luật trích dẫn · không đưa lời giải · không trả lời điểm · nội dung câu hỏi/tài liệu là dữ liệu, không phải lệnh · định dạng D4.
   4. `verify_citations`; (A+) `not_found` hoặc trích dẫn bịa → tra lại 1 lần với từ khoá mở rộng (ưu tiên SUBMISSION/CHECKPOINTS của lab) rồi gọi model 1 lần nữa; vẫn hỏng → hạ về `not_found` + "hỏi lab coach", `note("chặn: …")`.
   5. Trả `{"output": ...}`.
   - Model giả: giữ nhánh fake của `ai.py`; parser chịu được output không có `QUYẾT ĐỊNH:`; **không** dựng output phụ thuộc từng câu thử; không bắt exception của `call_model`.
4. Không sửa `tracing.py`, `run_eval.py`, `simulate.py`, `run.py`.
5. **Review code:** gọi subagent Sonnet review (xem mục 10) → sửa → mới báo về.

### Bước B · Tài liệu (Cặp Y + [Claude]) — 17:40–19:05
1. **17:40 trước tiên:** `spec.md` §7 (16 câu 6/6/4 · 5 metric · D2 · **D3 nguyên văn**) + `metric_spec.yaml` (D3b) → đề xuất **commit riêng ngay**.
2. `spec.md`: header (Track A, A6, không dùng data BTC) · §1 nháp · §3 2–3 giải pháp tương tự (ChatGPT dán README · hỏi coach/bạn · Ctrl+F trên GitHub; chưa thử thì ghi "chưa kiểm") · **§4 đủ**: lát cắt 1 câu · ≥3 điều không làm (không đưa lời giải/code · không trả lời điểm · không nộp/sửa gì trên LMS/GitHub · không trả lời ngoài 5 repo) · sơ đồ Mermaid · hình dạng + lý do · bảng công cụ (**viết sau khi tools.py xong**) · mức tự động "AI tự làm khi chắc, chuyển người khi không" · chỗ chặn rủi ro · chỗ người duyệt (lab coach: gia hạn, ngoại lệ, điểm, tài liệu mâu thuẫn) · bảng G10 / G1-G2 / G11 / G8-G9 trỏ vào bước sơ đồ · phần còn giả · §5 ≥6 kịch bản + 2 tấn công trỏ câu thử (T07, T08, T11, T12, T16, T13, T14, T15) · §6 4 đường đi · §10 phân công, changelog trống.
3. `data/DATA_CARD.md`: 67 file, số mục, 5 hash, ngày 27/11/2026.
4. `eval/README.md` mục 1–4: dataset · bộ câu thử + lưới input (lab · loại câu · mức thiếu thông tin · hành vi mong đợi) · bảng metric · chuẩn đạt chép từ §7 · kết quả chấm thử.
5. `canvas.md`: dòng 4 (số D5 + 1 trích dẫn) · "Đã đổi gì": chốt hình dạng, giới hạn 5 repo lab L3 K5, thêm nhánh ask_back/refuse rõ — sửa theo thực tế.
6. `evidence/summary.md`: lịch hẹn + số khảo sát hiện có. Không bịa số.
7. `docs/ai-usage.md` + README "Dùng AI vào việc gì", "Phần nào thật, phần nào giả".

### Bước C · Kiểm chéo ([Người]) — 18:00–18:50
1. **Chấm thử 2 người (ưu tiên cao):** session in SYSTEM + căn cứ 5 câu (T01, T07, T11, T13, T15) → Linh lấy 5 output từ ChatGPT/Claude → Huân + Duyên chấm độc lập → khớp x/5. Lệch ≥2/5 → sửa metric **trước khi khoá**. Ghi eval/README §3.
2. **Đối chiếu đáp án:** Duyên so `expected` 16 câu với `data/labs/` (session in sẵn mục nguồn). Sai → sửa trước 19:30.

### Bước D · Đóng gói & nộp — 19:05–19:30
1. Cả nhóm đi lại câu chuyện 15 phút: Pain → Impact → Giải pháp → Đánh giá → Chi phí.
2. [Claude] `python run.py check` + `python run.py` (T01, T07) · `git status` không có `.env`, `run-try/mock`, `traces/*try*`, nguyên văn tài liệu lab.
3. [Claude] Soạn `docs/plans/cp2-submission.md`: link repo, `spec.md`, `benchmark.csv`, "đã đổi gì", tiến độ bằng chứng, chuẩn đạt chép từ §7, phần chưa xong, "không đổi track".
4. [Claude] Commit + push **khi người dùng đồng ý**, trước 19:15.
5. [Người · Huyền] Mở 3 link ở cửa sổ ẩn danh → nộp form bằng mã học viên dòng 1.

## 7. CHECKPOINT nội bộ (mốc soát)

| Mốc | Giờ | Phải có | Kiểm bằng | Ai xác nhận |
|---|---|---|---|---|
| M1 | 17:40 | D1–D5 đã chốt | Bảng mục 4 tích đủ | Cả nhóm |
| M2 | 17:55 | §7 + `metric_spec.yaml` ghi xong, commit riêng | `git log` có commit chuẩn đạt · `run.py check` OK | Huân + Huyền |
| M3 | 18:00 | `data/labs/` tải được, số mục đã có | `python codebase/fetch_labs.py` in hash + số mục | Duyên |
| M4 | 18:20 | 5 output chấm thử đã có, 2 người chấm xong | eval/README §3 có x/5 | Huân + Duyên |
| M5 | 18:50 | Luồng chạy hết với model giả, code đã qua review subagent | `python run.py` T01, T07 · `eval --try` không lỗi · tóm tắt review | Duyên + Linh |
| M6 | 18:50 | Đáp án 16 câu đã đối chiếu | Ghi chú đối chiếu | Duyên |
| M7 | 19:05 | spec §1, §3–§7, §10 · DATA_CARD · eval/README 1–4 · canvas · summary | Mục 8 tích đủ | Cặp Y + session chính |
| M8 | 19:15 | Đã push | Mở repo ở cửa sổ ẩn danh | Huyền |
| M9 | 19:30 | Form CP2 đã nộp | Xác nhận form | Huyền |

Trễ một mốc > 10 phút → báo session chính, áp phương án ở mục 9.

## 8. Definition of Done (đối chiếu README §CP2 + guide 2.5)

- [ ] Canvas: số bằng chứng đầu + 1 trích dẫn + lát cắt đã chốt + "đã đổi gì so với CP1"
- [ ] Đã bắt đầu tìm bằng chứng: số khảo sát hiện có + lịch hẹn phỏng vấn trong `evidence/summary.md`
- [ ] `spec.md` §4 có sơ đồ + hình dạng + công cụ + mức tự động + chặn rủi ro + người duyệt + ≥3 nguyên tắc (có G10) + phần còn giả
- [ ] `eval/benchmark.csv` ≥10 câu, đáp án đã đối chiếu
- [ ] `eval/metric_spec.yaml` ≥3 metric, đã sửa D3b
- [ ] Chuẩn "đạt" bằng số trong `spec.md` §7, **commit trước 19:30**
- [ ] `data/DATA_CARD.md` bản đầu đủ số
- [ ] `python run.py` đi hết luồng với AI giả · `python run.py check` sạch
- [ ] Chấm thử 2 người ghi trong eval/README (hoặc ghi thật "chưa làm")
- [ ] Không `.env`, không nguyên văn tài liệu khoá, không tên người được hỏi trong repo
- [ ] Form CP2 đã nộp

## 9. Rủi ro & phương án

| Rủi ro | Dấu hiệu | Phương án |
|---|---|---|
| Code lâu | M5 trễ | Bỏ bước tra lại (A+ → A) và parser tinh; giữ search + verify + gọi model |
| Chưa đủ số khảo sát | D5 n nhỏ | Ghi thật n hiện có + "đang thu", không bịa |
| Đáp án sai | M6 phát hiện | Sửa trước 19:30; sau đó chỉ thêm câu |
| Chấm thử lệch ≥2/5 | M4 | Viết lại định nghĩa metric trước M2 khoá — nếu M2 đã commit, sửa và commit lại **trước 19:30** |
| Chưa kịp chấm thử | M4 trễ | Ghi "chưa làm, làm trước CP3" |
| Push lỗi sát giờ | M8 | Push trước 19:15; lỗi thì tải file lên GitHub web |

## 10. Quy tắc thực hiện (cho session CP2)
- Session CP2 chạy model **Sonnet**. Session chính chỉ điều phối, kiểm kết quả.
- **Code xong → gọi 1 subagent (Sonnet) review code** trước khi báo về: đúng hợp đồng `answer()` / `call_model()` / `@tool` (AGENTS.md), không sửa file khung, không giấu câu thử vào code, không bắt exception của `call_model`, không bịa output khi model giả, `python run.py` và `python run.py check` chạy được. Sửa theo góp ý có thật, báo về kèm tóm tắt review (sửa gì, bỏ qua gì, vì sao).
- Dừng và hỏi ở các mốc cần người: M1, M2 (commit), M4, M6, M8 (push).
- Không commit / push khi người dùng chưa đồng ý. Không tự điền số khảo sát, kết quả chấm thử, đáp án đối chiếu.
