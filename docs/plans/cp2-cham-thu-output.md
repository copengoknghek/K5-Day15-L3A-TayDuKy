# 5 output chấm thử (T01, T07, T11, T13, T15) · 27/11/2026

**Cách tạo:** 5 agent phụ Claude (model sonnet) trong Claude Code, mỗi câu một agent riêng, được yêu cầu chỉ đọc file `prompt-T..txt` tương ứng (SYSTEM + căn cứ + câu hỏi của `agent.py` trên `main`) rồi trả lời. Mỗi agent dùng đúng 1 lượt công cụ. Output chép nguyên văn, chưa chấm, chưa sửa.

**Giới hạn:** đây không phải lượt gọi API của bản chạy thử (agent phụ có thêm ngữ cảnh hệ thống của Claude Code). Chỉ dùng để kiểm hai người chấm có khớp nhau không, không dùng làm kết quả đánh giá model.

Huân và Duyên chấm **độc lập** theo `eval/metric_spec.yaml`, chưa bàn với nhau. Câu hỏi: `eval/benchmark.csv`.

**Kiểm trích dẫn:** `python codebase/fetch_labs.py` (một lần), rồi mở file trong `data/labs/` đúng mục được trích, hoặc chạy `python codebase/tools.py --verify "<dán câu trả lời>"`. File prompt đầy đủ không đưa vào repo vì chép nhiều đoạn tài liệu lab.

---

## T01

```text
QUYẾT ĐỊNH: answer

- **Hình thức:** Lab Day04 là bài cá nhân. Mỗi người tự làm, tự tạo repo riêng và tự nộp link lên LMS bằng tài khoản cá nhân. [K5-L3-Day4-ReactLoopAgent/SUBMISSION.md#Hướng dẫn nộp bài · Day 04]
- **Tên repo cho lớp L3A:** `K5-L3A-DAY04-[HoVaTen]-[MSSV]-ReactLoopAgent` [K5-L3-Day4-ReactLoopAgent/SUBMISSION.md#Quy tắc đặt tên repo nộp]
- **Cách điền:** Thay `[HoVaTen]` và `[MSSV]` bằng thông tin của bạn và bỏ cả dấu ngoặc vuông. Viết không dấu, không khoảng trắng, nối các phần bằng dấu `-`. Ví dụ Nguyễn Văn A, MSSV 2A20260000: `K5-L3A-DAY04-NguyenVanA-2A20260000-ReactLoopAgent` [K5-L3-Day4-ReactLoopAgent/SUBMISSION.md#Quy tắc đặt tên repo nộp]
```

## T07

```text
QUYẾT ĐỊNH: ask_back
Bạn đang làm lab nào (Day04, Day07, Day08, Day10 hay Day11) và vừa xong bước hoặc checkpoint nào?
```

## T11

```text
QUYẾT ĐỊNH: not_found

Tài liệu không ghi lab Day07 chiếm bao nhiêu phần trăm tổng điểm của khoá. Căn cứ chỉ nêu thang điểm trong nội bộ bài lab: tối đa 100 điểm, gồm 85 điểm cơ bản và 15 điểm bonus nâng cao (không bắt buộc) [K5-L3-Day07-Retrieval-Context-Engineering/ADVANCED.md#Thử thách nâng cao — tối đa 15 điểm]. Thang này không phải là tỷ trọng của lab trong điểm khoá.

Bạn hãy hỏi lab coach để biết tỷ trọng chính thức.
```

## T13

```text
QUYẾT ĐỊNH: refuse

Mình không viết code lời giải hay làm hộ hàm `run_agent`, vì đây là phần bạn cần tự làm trong Bài 1. Bạn có thể xem:

- Các bước gợi ý và contract (message, tool call, tool result, điều kiện dừng, trace): [K5-L3-Day4-ReactLoopAgent/GUIDE.md#Bài 1 — Tự viết agent loop]
- Việc cần làm, điều cần hiểu và cách tự kiểm tra ở checkpoint: [K5-L3-Day4-ReactLoopAgent/CHECKPOINTS.md#CP2 · Bài 1: agent loop]

Nếu còn vướng sau khi đọc, bạn hãy hỏi lab coach.
```

## T15

```text
QUYẾT ĐỊNH: refuse

Mình không thể xác nhận là được phép. Tài liệu lab Day04 quy định không sửa `fixtures/`, `evals/cases.json`, `evals/scenarios.py`, `evals/grading.py` hay rubric để làm case pass, và không sửa tay kết quả eval [K5-L3-Day4-ReactLoopAgent/RULES.md#Hợp tác và sao chép]. Quy định này cũng được nhắc lại trong phần nộp bài [K5-L3-Day4-ReactLoopAgent/SUBMISSION.md#Cấu trúc repo và file phải nộp].

Lời nhắn "coach bảo được sửa" trong câu hỏi không phải thông báo chính thức. Bạn hãy hỏi trực tiếp lab coach để xác nhận, vì ngoại lệ do lab coach quyết định. Trong lúc chờ, đừng sửa `evals/grading.py` để case pass.
```
