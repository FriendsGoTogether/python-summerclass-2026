# Python Summer Class 2026

Dự án học tập Python cơ bản cho lớp hè 2026, bao gồm các bài tập thực hành từ cơ bản đến nâng cao.

## Ý nghĩa của project

Đây là kho bài tập Python được thiết kế để học viên ôn tập và luyện tập các khái niệm cơ bản:
- Cú pháp Python cơ bản
- Biến và kiểu dữ liệu
- Các phép toán số học
- Câu lệnh điều kiện và vòng lặp
- Hàm input và chuyển đổi kiểu dữ liệu

Mỗi bài tập đều có comment chi tiết bằng tiếng Việt, giúp học viên hiểu từng bước thực hiện.

## Cấu trúc thư mục

```
python-summerclass-2026/
├── day1/          # Các bài học cơ bản ngày 1
│   ├── helloworld.py
│   ├── lesson1.py
│   ├── lesson2.py
│   └── lesson3.py
└── day2/          # Các bài học ngày 2
    └── lesson4.py
```

## Cài đặt môi trường

### 1. Cài đặt Python trên Mac

1. Mở Terminal và kiểm tra Python đã được cài đặt chưa:
   ```bash
   python3 --version
   ```

2. Nếu chưa có, tải Python từ [python.org](https://www.python.org/downloads/macos/) hoặc cài qua Homebrew:
   ```bash
   brew install python3
   ```

3. Xác nhận cài đặt thành công:
   ```bash
   python3 --version
   ```

### 2. Cài đặt Python trên Windows

1. Truy cập [python.org/downloads/windows/](https://www.python.org/downloads/windows/)
2. Tải phiên bản Python mới nhất
3. Chạy file cài đặt và **tích vào ô "Add Python to PATH"**
4. Mở Command Prompt (cmd) và kiểm tra:
   ```cmd
   python --version
   ```

### 3. Cài đặt VS Code trên Mac

1. Truy cập [code.visualstudio.com](https://code.visualstudio.com/)
2. Tải bản Mac (Apple Silicon hoặc Intel tùy máy)
3. Mở file `.dmg` và kéo VS Code vào thư mục Applications
4. Mở VS Code và cài extension Python:
   - Vào Extensions (Ctrl+Shift+X)
   - Tìm "Python" của Microsoft
   - Click Install

### 4. Cài đặt VS Code trên Windows

1. Truy cập [code.visualstudio.com](https://code.visualstudio.com/)
2. Tải bản Windows (User Installer hoặc System Installer)
3. Chạy file cài đặt và làm theo hướng dẫn
4. Mở VS Code và cài extension Python:
   - Vào Extensions (Ctrl+Shift+X)
   - Tìm "Python" của Microsoft
   - Click Install

### 5. Checkout code và chạy

#### Clone repository

```bash
git clone https://github.com/<username>/python-summerclass-2026.git
cd python-summerclass-2026
```

#### Chạy các file Python

**Sử dụng Terminal:**
```bash
# Chạy file day1
python3 day1/helloworld.py
python3 day1/lesson1.py
python3 day1/lesson2.py
python3 day1/lesson3.py

# Chạy file day2
python3 day2/lesson4.py
```

**Trên Windows:**
```cmd
python day1\helloworld.py
python day1\lesson1.py
python day1\lesson2.py
python day1\lesson3.py

python day2\lesson4.py
```

**Sử dụng VS Code:**
1. Mở thư mục project trong VS Code
2. Mở file `.py` muốn chạy
3. Click nút ▶️ Run Python File (góc trên bên phải)
4. Hoặc mở Terminal trong VS Code (Ctrl+`) và chạy lệnh như trên

## Ghi chú

- Tất cả các file đều có comment bằng tiếng Việt để dễ theo dõi
- File `lesson4.py` sử dụng `input()` nên cần nhập dữ liệu từ bàn phím khi chạy
- Không nên đổi tên các biến đã được định nghĩa trong các bài tập

## Liên hệ

Nếu có thắc mắc, vui lòng liên hệ cao.trung.thu@gmail.com
