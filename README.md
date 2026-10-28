# Kiểm thử tự động với Selenium – SauceDemo

**Sinh viên:** Hoàng Trung Tuyến – MSSV: `<23010188>`
**Môn học:** `<Đánh giá và kiểm định phần mềm>` – GV: `<Trịnh Thanh Bình>`

## 1. Giới thiệu
Selenium là bộ công cụ mã nguồn mở dùng để tự động hóa trình duyệt web. Selenium WebDriver
điều khiển trình duyệt thật (Chrome, Firefox, Edge...) giống như người dùng: mở trang, nhập
liệu, click, đọc nội dung, từ đó kiểm tra website có hoạt động đúng hay không.

Website được kiểm thử: **https://www.saucedemo.com** – trang bán hàng demo dành cho việc
luyện tập kiểm thử, có đầy đủ chức năng đăng nhập, giỏ hàng, thanh toán, đăng xuất.

## 2. Công nghệ sử dụng
| Thành phần | Vai trò |
|---|---|
| Python 3.x | Ngôn ngữ viết test |
| Selenium 4 | Điều khiển trình duyệt (tự tải ChromeDriver qua Selenium Manager) |
| pytest | Framework chạy test, quản lý fixture |
| pytest-html | Xuất báo cáo kết quả dạng HTML |
| Google Chrome | Trình duyệt chạy test |

## 3. Cấu trúc thư mục
```
selenium-testing/
├── conftest.py          # Fixture khởi tạo/đóng trình duyệt, chụp ảnh khi fail
├── utils.py             # Hàm dùng chung: login, đếm giỏ hàng
├── tests/
│   ├── test_login.py    # TC01–TC04: đăng nhập
│   └── test_shopping.py # TC05–TC09: giỏ hàng, sắp xếp, thanh toán, đăng xuất
├── screenshots/         # Ảnh chụp kết quả
├── requirements.txt
└── pytest.ini
```

## 4. Cài đặt và chạy
```bash
git clone <link-repo-cua-ban>
cd selenium-testing
python -m venv venv
venv\Scripts\activate        # Windows  (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt

pytest                                   # chạy toàn bộ test
pytest --html=report.html --self-contained-html   # chạy và xuất báo cáo HTML
```

## 5. Danh sách test case
| ID | Chức năng | Các bước | Dữ liệu | Kết quả mong đợi | Kết quả |
|---|---|---|---|---|---|
| TC01 | Đăng nhập thành công | Nhập user, pass → Login | standard_user / secret_sauce | Vào trang Products | Pass |
| TC02 | Đăng nhập sai mật khẩu | Nhập pass sai → Login | standard_user / sai_mat_khau | Báo lỗi "do not match" | Pass |
| TC03 | Tài khoản bị khóa | Đăng nhập user bị khóa | locked_out_user | Báo lỗi "locked out" | Pass |
| TC04 | Bỏ trống thông tin | Bấm Login khi để trống | (trống) | Báo lỗi "Username is required" | Pass |
| TC05 | Thêm vào giỏ hàng | Add Backpack → mở giỏ | Sauce Labs Backpack | Badge = 1, sản phẩm có trong giỏ | Pass |
| TC06 | Xóa khỏi giỏ hàng | Add → Remove | Sauce Labs Backpack | Badge biến mất | Pass |
| TC07 | Sắp xếp theo giá tăng dần | Chọn "Price (low to high)" | lohi | Giá tăng dần | Pass |
| TC08 | Thanh toán | Add → Checkout → nhập thông tin → Finish | Tuyen / Hoang / 700000 | "Thank you for your order!" | Pass |
| TC09 | Đăng xuất | Mở menu → Logout | – | Quay về trang đăng nhập | Pass |

> Cột "Kết quả" cập nhật theo kết quả chạy thực tế.

## 6. Kết quả chạy
![Kết quả pytest](screenshots/ket-qua.png)


## 7. Nhận xét
- Ưu điểm của Selenium: miễn phí, hỗ trợ nhiều ngôn ngữ và trình duyệt, chạy lặp lại nhanh,
  phù hợp kiểm thử hồi quy.
- Hạn chế: phụ thuộc vào cấu trúc HTML (đổi ID là test hỏng), cần xử lý chờ (wait) cho phần
  tử tải chậm, không kiểm thử được những gì ngoài trình duyệt.
- Bài học: dùng `WebDriverWait` thay cho `time.sleep`, tách hàm dùng chung (login) để code gọn,
  ưu tiên locator ổn định như `id`, `data-test`.

## 8. Tài liệu tham khảo
- https://www.selenium.dev/documentation/
- https://docs.pytest.org/
