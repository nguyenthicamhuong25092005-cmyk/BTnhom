# 📐 Tích Hợp CNTT Trong Dạy Học Toán: Ứng Dụng Thư Viện SymPy & Matplotlib 3D Tính Thể Tích Bằng Tích Phân

> **Đề tài nghiên cứu khoa học xây dựng hệ thống thuật toán tự động hóa đại số ký hiệu và kết xuất mô hình đồ họa không gian 3D tương tác động phục vụ dạy học chủ đề Thể tích khối tròn xoay.**

---

## 📌 1. Thông tin chung

*   **Tên đề tài:** Ứng dụng thư viện SymPy và Matplotlib 3D để tính thể tích bằng tích phân và trực quan hoá hình ảnh.
*   **Nhóm sinh viên thực hiện:** Phạm Phương Linh, Hoàng Ngọc Hùng, Nguyễn Thị Cẩm Hương, Đặng Thanh Quý.
*   **Giảng viên hướng dẫn:** TS. Nguyễn Đăng Minh Phúc.
*   **Thời gian hoàn thành:** Tháng 10/2026.
*   **Định dạng đầu ra:**
*   - file PDF hoàn chỉnh: gồm 39 trang
    -  file readme.md giới thiệu tổng quan về dự án
    -  file mã nguồn trong sympy và matplotlib gồm các file: quay_quanh_Ox.py; quay_quanh_Oy.py; 2ham_quanh_Ox.py; tinh_nguyen_ham_tp.py;dư_an.py
    -  file mã latex: code trong latex.txt
*   **Link overleaf:** https://www.overleaf.com/read/hsvhfvnwvhft#751c50

---

## 📂 2. Cấu trúc mã nguồn & Thư mục dự án đề xuất

```text
├── README.md               # Tệp giới thiệu tổng quan hệ thống phần mềm
├── main.py                 # Điểm kích hoạt chương trình chính (Giao diện tích hợp)
├── source/                 # Thư mục quản lý các module mã nguồn Python
│   ├── basic_calculus.py   # Tính toán nguyên hàm, tích phân xác định độc lập (SymPy)
│   ├── volume_ox.py        # Module tính thể tích & dựng hình khối tròn xoay quanh Ox
│   ├── volume_oy.py        # Module tính thể tích & dựng hình khối tròn xoay quanh Oy
│   └── volume_intersection.py # Module xử lý miền phẳng giao nhau giữa hai đồ thị
└── requirements.txt        # Tài liệu định nghĩa các thư viện phụ thuộc
```

---

## 📚 3. Đề cương cấu trúc tiểu luận

### 📑 Phần mở đầu
*   **Thực trạng:** Quỹ thời gian môn Toán ở phổ thông hạn chế (4 tiết/tuần). Việc vẽ phấn bảng các đồ thị cong phức tạp (sin, parabol) ngốn từ 5-10 phút, gây thiếu hụt thời gian thực hành và rào cản tư duy không gian cho học sinh.
*   **Ý tưởng cải tiến:** Kế thừa giải pháp trực quan hóa từ công nghệ in 3D vật lý (mất thời gian chế tác). Đề tài can thiệp bằng lập trình phần mềm máy tính qua **ngôn ngữ Python** để xuất mô hình 3D động ngay lập tức.

### 💡 Chương 1: Kiến thức chuẩn bị
*   **Cơ sở toán học:** Định nghĩa khái niệm nguyên hàm, họ nguyên hàm, tính chất tuyến tính và định lý Newton-Leibniz cốt lõi.
*   **Công cụ lập trình:** Tổng quan cú pháp khai báo toán ký hiệu từ `SymPy` (biến, hằng số `pi`, vô cực `oo`) và module thiết lập hệ trục tọa độ Descartes không gian Oxyz `Matplotlib 3D`.

### 🖥️ Chương 2: Ứng dụng SymPy trong tính nguyên hàm & tích phân
*   Thiết lập bộ tiếp nhận chuỗi ký tự thô từ bàn phím qua hàm `input()`.
*   Ứng dụng thuật toán hạt nhân `sp.sympify()` để dịch mã văn bản thành biểu thức toán học và gọi lệnh `sp.integrate()` xử lý tự động.

### 🌀 Chương 3: Ứng dụng SymPy & Matplotlib 3D trong tính thể tích
Giải quyết khép kín ba dạng toán tích phân trọng tâm kèm theo sơ đồ thuật toán tự động hóa:
1.  **Khối tròn xoay quay quanh trục Ox:** 
    *   *Công thức:* $V = \pi \int_{a}^{b} [f(x)]^2 dx$.
    *   *Lệnh thực thi:* `V = sp.pi * sp.integrate(f**2, (x, a, b))`.
2.  **Khối tròn xoay quay quanh trục Oy:**
    *   *Công thức:* $V = \pi \int_{c}^{d} [g(y)]^2 dy$. 
    *   *Lệnh thực thi:* `V = sp.pi * sp.integrate(g**2, (y, c, d))`.
3.  **Miền tạo bởi giao nhau giữa hai đồ thị (\(y=f(x)\) và \(y=g(x)\)) quanh Ox:**
    *   *Công thức:* $V = \pi \int_{a}^{b}|f^2(x) - g^2(x)| dx$.
    *   *Cơ chế:* Sử dụng `sp.solve()` để quét tìm giao điểm, lọc nghiệm thực an toàn qua thuộc tính `.is_real`, phân định bán kính trong/ngoài bằng hàm `maximum/minimum` để hiển thị vật thể rỗng lòng.

### 📊 Chương 4: Đánh giá — Tổng kết
*   **Kết quả:** Hệ thống chạy ổn định, rút ngắn thời gian thiết kế học liệu 3D xuống chỉ còn **3 đến 5 giây** (thay thế cho 15-20 phút thao tác trên các ứng dụng vẽ 3D truyền thống).
*   **Hạn chế:** Tiểu luận mang tính lý thuyết mã nguồn, **chưa có số liệu thực nghiệm sư phạm** tại lớp học phổ thông. Giao diện hiển thị dạng dòng lệnh (Terminal/Cmd) còn thô và là rào cản với giáo viên không chuyên CNTT.

---

## ⚡ 4. Hướng dẫn cài đặt & Chạy ứng dụng

### Yêu cầu hệ thống
*   Máy tính đã cài đặt sẵn **Python 3.x**.

### Cài đặt các thư viện phụ thuộc
Mở Terminal/Command Prompt trên máy tính của bạn và thực thi dòng lệnh cài đặt các gói module toán học và đồ họa:
```bash
pip install numpy matplotlib sympy
```

### Chạy chương trình
```bash
python main.py
```
## 5. Thời gian thực hiện đề tài:
🪷 Tuần 1:

- Thu thập tài liệu tham khảo, sách giáo khoa, giáo trình và các tài liệu nghiên cứu liên quan đến Tích phân và cách ứng dụng CNTT vào dạy học Toán.

- Tiến hành viết phần mở đầu; vạch khung ý tưởng và xây dựng đề cương chi tiết cho các Chương 1, Chương 2 và Chương 3.

- Tìm hiểu cách ứng dụng thư viện SymPy (tính tích phân) và Matplotlib 3D (dựng mô hình khối tròn xoay) trong Python.

🪷 Tuần 2:

- Định dạng mục lục tự động và thiết lập danh mục tài liệu tham khảo theo chuẩn.

- Hoàn thiện và rà soát lại nội dung chi tiết các chương.

- Dựa vào tài liệu tham khảo để tìm, chọn lọc và giải bài tập minh họa của từng dạng bài tính thể tích bằng tích phân.

🪷 Tuần 3:

- Viết mã nguồn Python kết hợp SymPy và Matplotlib 3D để giải và trực quan hóa các bài tập minh họa đã chọn.

- Đánh giá hiệu quả trực quan của mô hình 3D tương tác động trong việc hỗ trợ tư duy không gian cho học sinh (chương 4).

- Rà soát toàn bộ văn bản, chỉnh sửa lỗi trình bày, hoàn thiện báo cáo tổng kết và chuẩn bị nghiệm thu đề tài. 
## 📋 6. Danh mục tài liệu tham khảo chính

1.  Bộ Giáo dục và Đào tạo (2024). *Toán 12 (Tập 2)*. Nhà xuất bản Giáo dục Việt Nam.
2.  Nguyễn Đăng Minh Phúc, Phạm Thị Mỹ Nhân (2023). Ứng dụng công nghệ in 3D hỗ trợ dạy học chủ đề “Thể tích khối tròn xoay” (Toán 12). *Tạp chí Giáo dục*, 23(23). Truy xuất từ: https://tapchigiaoduc.edu.vn
3.  SymPy Development Team (2023). *SymPy: Python library for symbolic mathematics*. Truy xuất từ: https://sympy.org
4.  Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. *Computing in Science & Engineering*, 9(3), 90–95.
5.  Van Rossum, G., & Drake, F. L. (2009). *Python 3 Reference Manual*. CreateSpace.
