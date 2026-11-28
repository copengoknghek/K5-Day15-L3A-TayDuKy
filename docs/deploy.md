# Chạy và deploy bản web

Web nằm ở `codebase/web.py` và `codebase/static/`. Nó gọi `answer()` trong `agent.py`, không có luồng riêng.
Chỉ dùng thư viện chuẩn, không cần `pip install`.

| Trang | Địa chỉ | Có gì |
|---|---|---|
| Trang chủ | `/` | giới thiệu, số lab / file / mục, kết quả lượt đánh giá mới nhất |
| Hỏi bot | `/bot` | khung hội thoại, chọn lab; câu không nêu lab thì được gắn lab đã chọn |

Bot chỉ nhớ số lab của câu trước (như `python run.py`), không nhớ nội dung; trình duyệt giữ số đó, mỗi người một phiên.
Lịch sử trò chuyện (tối đa 20 cuộc) lưu trong `localStorage` của trình duyệt, không gửi lên máy chủ; xoá được trên trang.

## Chạy trên máy

```powershell
python codebase/fetch_labs.py
```

```powershell
python codebase/web.py
```

Mở http://localhost:8000. Model lấy theo `.env`; chưa có `.env` thì chạy chế độ giả.

## Deploy lên Render

1. Commit và push code web lên GitHub.
2. Đặt hạn mức chi tiêu cho API key trên trang nhà cung cấp model.
3. Đăng nhập https://render.com → **New** → **Blueprint** → chọn repo của nhóm. Render đọc `render.yaml`.
4. Khi được hỏi `API_KEY`, tự dán key. Không ghi key vào file nào trong repo.
5. Chờ build xong, mở địa chỉ `https://….onrender.com` Render cấp và hỏi thử một câu.

Gói miễn phí thường cho máy chủ ngủ khi không ai vào, lần mở đầu sẽ chậm: mở trang trước khi demo.
Kiểm điều kiện gói lúc đăng ký.

## Giới hạn dùng

Ai có link đều hỏi được bằng key của nhóm. Mặc định: câu hỏi tối đa 500 ký tự, 6 câu/phút mỗi địa chỉ,
200 câu/ngày. Đổi bằng biến môi trường `WEB_PER_MINUTE`, `WEB_PER_DAY`.
Bộ đếm nằm trong bộ nhớ nên về 0 khi máy chủ khởi động lại: hạn mức chi tiêu ở bước 2 mới là chặn chắc.
Demo xong thì tắt dịch vụ hoặc thu hồi key.

## Số hiện trên trang

Đọc trực tiếp lúc mở trang: số lab, file, mục từ `data/labs/`; biểu đồ từ `eval/run-N.csv` mới nhất.
Cột `pass` đã chấm đủ thì trang hiện số câu **đạt**; chưa chấm thì chỉ hiện số câu **đúng nhánh**
(so nhánh quyết định với nhãn đầu cột `expected`), không phải điểm đạt.
