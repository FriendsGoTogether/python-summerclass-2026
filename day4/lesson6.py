# Bài 6: Câu lệnh điều kiện if, elif, else trong Python
# Bài này luyện cách dùng if để kiểm tra một điều kiện và rẽ nhánh chương trình.

# Ví dụ 1: Kiểm tra số dương
# if chỉ chạy khối lệnh bên trong khi điều kiện đúng
x = int(input())
if x > 0:
    print("Số dương")

# Ví dụ 2: Kiểm tra số dương hoặc không phải số dương
# else chạy khi điều kiện của if sai
x = int(input())
if x > 0:
    print("Số dương")
else:
    print("Không phải số dương")

# Ví dụ 3: Kiểm tra số dương, số âm hoặc bằng 0
# elif dùng để kiểm tra thêm điều kiện khi các điều kiện trước sai
x = int(input())
if x > 0:
    print("Số dương")
elif x < 0:
    print("Số âm")
else:
    print("Số bằng 0")

# Ví dụ 4: Xếp loại điểm bằng nhiều điều kiện
# Chương trình kiểm tra từ điều kiện cao nhất xuống thấp nhất
score = int(input())
if score >= 9:
    print("A")
elif score >= 8:
    print("B")
elif score >= 7:
    print("C")
elif score >= 5:
    print("D")
else:
    print("F")
