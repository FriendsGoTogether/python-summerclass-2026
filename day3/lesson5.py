# Bài 5: Các phép toán số học và so sánh trong Python
# Bài này giới thiệu các toán tử cơ bản trong Python:
# - Toán tử số học: +, -, *, /, //, %, **
# - Toán tử gán rút gọn: +=, *=, -=, //=, %=
# - Hàm toán học: max, min, abs, ceil, sqrt
# - Toán tử so sánh: ==, !=, >=, <=, >, <
# - Toán tử logic: and, or

import math  # Thư viện cung cấp các hàm toán học như ceil và sqrt

print("=== Bước 1: Gán biến a ===")
a = 16  # Gán biến a bằng 16
print("a =", a)

print("\n=== Bước 2: Gán biến b ===")
b = 3  # Gán biến b bằng 3
print("b =", b)

print("\n=== Bước 3: Phép cộng ===")
result = a + b  # Tính tổng a và b
print("a + b =", result)

print("\n=== Bước 4: Phép trừ ===")
result = a - b  # Tính hiệu a và b
print("a - b =", result)

print("\n=== Bước 5: Phép nhân ===")
result = a * b  # Tính tích a và b
print("a * b =", result)

print("\n=== Bước 6: Phép chia ===")
result = a / b  # Tính thương a và b; phép chia / luôn trả về số thực
print("a / b =", result)

print("\n=== Bước 7: Phép chia lấy phần nguyên ===")
result = a // b  # Chia lấy phần nguyên, kết quả là phần nguyên của thương
print("a // b =", result)

print("\n=== Bước 8: Phép chia lấy dư ===")
result = a % b  # Chia lấy phần dư, kết quả là số dư sau khi chia a cho b
print("a % b =", result)

print("\n=== Bước 9: Phép luỹ thừa ===")
result = a ** b  # Tính a lũy thừa b, tức là 16 mũ 3
print("a ** b =", result)

print("\n=== Bước 10: Gán lại a ===")
a = 10  # Gán lại biến a bằng 10 để chuẩn bị cho các phép gán rút gọn
print("a =", a)

print("\n=== Bước 11: Cộng gán a += 2 ===")
a += 2  # Tương đương a = a + 2: cộng 2 vào a rồi gán lại cho a
print("a sau khi += 2:", a)

print("\n=== Bước 12: Nhân gán a *= 2 ===")
a *= 2  # Tương đương a = a * 2: nhân a với 2 rồi gán lại cho a
print("a sau khi *= 2:", a)

print("\n=== Bước 13: Trừ gán a -= 2 ===")
a -= 2  # Tương đương a = a - 2: trừ 2 khỏi a rồi gán lại cho a
print("a sau khi -= 2:", a)

print("\n=== Bước 14: Chia lấy phần nguyên gán a //= 2 ===")
a //= 2  # Tương đương a = a // 2: chia lấy phần nguyên rồi gán lại cho a
print("a sau khi //= 2:", a)

print("\n=== Bước 15: Chia lấy dư gán a %= 2 ===")
a %= 2  # Tương đương a = a % 2: chia lấy dư rồi gán lại cho a
print("a sau khi %= 2:", a)

print("\n=== Bước 16: Tìm giá trị lớn nhất ===")
print("max(a, b):", max(a, b))

print("\n=== Bước 17: Tìm giá trị nhỏ nhất ===")
print("min(a, b):", min(a, b))

print("\n=== Bước 18: Giá trị tuyệt đối của a - b ===")
print("abs(a - b):", abs(a - b))

print("\n=== Bước 19: Giá trị tuyệt đối của b - a ===")
print("abs(b - a):", abs(b - a))

print("\n=== Bước 20: Làm tròn lên sau phép chia lấy phần nguyên ===")
print("math.ceil(b // a):", math.ceil(b // a))

print("\n=== Bước 21: Căn bậc hai của a ===")
print("math.sqrt(a):", math.sqrt(a))

print("\n=== Bước 22: Gán biến để so sánh ===")
A = 10  # Gán A = 10
B = 12  # Gán B = 12
C = 10  # Gán C = 10

print("\n=== Bước 23: So sánh bằng (==) ===")
print("A == B (10 == 12):", A == B)  # Kiểm tra A có bằng B không, kết quả là False
print("A == C (10 == 10):", A == C)  # Kiểm tra A có bằng C không, kết quả là True

print("\n=== Bước 24: So sánh khác (!=) ===")
print("A != C (10 != 10):", A != C)  # Kiểm tra A có khác C không, kết quả là False
print("A != B (10 != 12):", A != B)  # Kiểm tra A có khác B không, kết quả là True

print("\n=== Bước 25: So sánh lớn hơn hoặc bằng (>=) ===")
print("A >= B (10 >= 12):", A >= B)  # Kiểm tra A có lớn hơn hoặc bằng B không, kết quả là False
print("A >= C (10 >= 10):", A >= C)  # Kiểm tra A có lớn hơn hoặc bằng C không, kết quả là True

print("\n=== Bước 26: So sánh nhỏ hơn hoặc bằng (<=) ===")
print("A <= B (10 <= 12):", A <= B)  # Kiểm tra A có nhỏ hơn hoặc bằng B không, kết quả là True
print("A <= C (10 <= 10):", A <= C)  # Kiểm tra A có nhỏ hơn hoặc bằng C không, kết quả là True

print("\n=== Bước 27: So sánh lớn hơn (>) ===")
print("A > B (10 > 12):", A > B)  # Kiểm tra A có lớn hơn B không, kết quả là False
print("A > C (10 > 10):", A > C)  # Kiểm tra A có lớn hơn C không, kết quả là False

print("\n=== Bước 28: So sánh nhỏ hơn (<) ===")
print("A < B (10 < 12):", A < B)  # Kiểm tra A có nhỏ hơn B không, kết quả là True
print("A < C (10 < 10):", A < C)  # Kiểm tra A có nhỏ hơn C không, kết quả là False

print("\n=== Bước 29: Toán tử logic AND (và) ===")
# and chỉ trả về True khi cả hai điều kiện đều đúng
print("A > 10 and B > 10 (10 > 10 and 12 > 10):", A > 10 and B > 10)

print("\n=== Bước 30: Toán tử logic OR (hoặc) ===")
# or trả về True nếu ít nhất một trong hai điều kiện đúng
print("A > 10 or B > 10 (10 > 10 or 12 > 10):", A > 10 or B > 10)
