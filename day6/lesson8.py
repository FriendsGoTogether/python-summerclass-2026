# 1. Mặc định bắt đầu từ 0 và dừng trước 5 (tăng 1 đơn vị)
# Dãy số tạo ra: 0, 1, 2, 3, 4
i = 0
while i < 5:
    print(i)
    i += 1

# 2. Lặp lại một hành động (không dùng đến biến i trong thân vòng lặp)
# Vòng lặp chạy đúng 5 lần
i = 0
while i < 5:
    print("Thanks")
    i += 1

# 3. Biến tấu giá trị i bằng cách cộng thêm 1 khi in
# Dãy số gốc của i: 0, 1, 2, 3, 4 -> cộng thêm 1 sẽ thành: 1, 2, 3, 4, 5
i = 0
while i < 5:
    print(i + 1)
    i += 1

# 4. Chỉ định điểm bắt đầu là 1 và dừng trước 6 (tăng 1 đơn vị)
# Dãy số tạo ra: 1, 2, 3, 4, 5
i = 1
while i < 6:
    print(i)
    i += 1

# 5. Bắt đầu từ 10 và dừng trước 51 (tăng 1 đơn vị)
# Dãy số tạo ra: 10, 11, 12, ..., 49, 50
i = 10
while i < 51:
    print(i)
    i += 1

# 6. Bắt đầu từ 1, dừng trước 101, bước nhảy là 2 (Đếm cách 2 đơn vị)
# Dãy số tạo ra: 1, 3, 5, 7, ..., 97, 99
i = 1
while i < 101:
    print(i)
    i += 2

# 7. Bắt đầu từ 10, dừng trước 51, bước nhảy là 2 
# Dãy số tạo ra: 10, 12, 14, ..., 48, 50
i = 10
while i < 51:
    print(i)
    i += 2

# 8. Đếm ngược: Bắt đầu từ 100, dừng trước 0, bước nhảy là -1 (Trừ 1 đơn vị)
# Dãy số tạo ra: 100, 99, 98, ..., 2, 1
i = 100
while i > 0:
    print(i)
    i -= 1

# 9. Đếm ngược cách 2: Bắt đầu từ 100, dừng trước 9, bước nhảy là -2 (Trừ 2 đơn vị)
# Dãy số tạo ra: 100, 98, 96, ..., 12, 10
i = 100
while i > 9:
    print(i)
    i -= 2