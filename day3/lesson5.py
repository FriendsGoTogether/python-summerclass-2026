# Bài 5: Các phép toán số học và so sánh trong Python

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
result = a / b  # Tính thương a và b (trả về số thực)
print("a / b =", result)

print("\n=== Bước 7: Phép chia lấy phần nguyên ===")
result = a // b  # Chia lấy phần nguyên
print("a // b =", result)

print("\n=== Bước 8: Phép chia lấy dư ===")
result = a % b  # Chia lấy phần dư
print("a % b =", result)

print("\n=== Bước 9: Phép luỹ thừa ===")
result = a ** b  # Tính a lũy thừa b (16^3)
print("a ** b =", result)

print("\n=== Bước 10: Gán lại a ===")
a = 10  # Gán lại biến a bằng 10
print("a =", a)

print("\n=== Bước 11: Cộng gán a += 2 ===")
a += 2  # a = a + 2, cộng 2 vào a rồi gán lại cho a
print("a += 2 => a =", a)

print("\n=== Bước 12: Nhân gán a *= 2 ===")
a *= 2  # a = a * 2, nhân a với 2 rồi gán lại cho a
print("a *= 2 => a =", a)

print("\n=== Bước 13: Trừ gán a -= 2 ===")
a -= 2  # a = a - 2, trừ 2 khỏi a rồi gán lại cho a
print("a -= 2 => a =", a)

print("\n=== Bước 14: Chia lấy phần nguyên gán a //= 2 ===")
a //= 2  # a = a // 2, chia lấy phần nguyên rồi gán lại cho a
print("a //= 2 => a =", a)

print("\n=== Bước 15: Chia lấy dư gán a %= 2 ===")
a %= 2  # a = a % 2, chia lấy dư rồi gán lại cho a
print("a %= 2 => a =", a)

print("\n=== Bước 16: Gán biến để so sánh ===")
A = 10  # Gán A = 10
B = 12  # Gán B = 12
C = 10  # Gán C = 10

print("\n=== Bước 17: So sánh bằng (==) ===")
print("A == B (10 == 12):", A == B)  # So sánh A có bằng B không
print("A == C (10 == 10):", A == C)  # So sánh A có bằng C không

print("\n=== Bước 18: So sánh khác (!=) ===")
print("A != C (10 != 10):", A != C)  # So sánh A có khác C không
print("A != B (10 != 12):", A != B)  # So sánh A có khác B không

print("\n=== Bước 19: So sánh lớn hơn hoặc bằng (>=) ===")
print("A >= B (10 >= 12):", A >= B)  # So sánh A có lớn hơn hoặc bằng B không
print("A >= C (10 >= 10):", A >= C)  # So sánh A có lớn hơn hoặc bằng C không

print("\n=== Bước 20: So sánh nhỏ hơn hoặc bằng (<=) ===")
print("A <= B (10 <= 12):", A <= B)  # So sánh A có nhỏ hơn hoặc bằng B không
print("A <= C (10 <= 10):", A <= C)  # So sánh A có nhỏ hơn hoặc bằng C không

print("\n=== Bước 21: So sánh lớn hơn (>) ===")
print("A > B (10 > 12):", A > B)  # So sánh A có lớn hơn B không
print("A > C (10 > 10):", A > C)  # So sánh A có lớn hơn C không

print("\n=== Bước 22: So sánh nhỏ hơn (<) ===")
print("A < B (10 < 12):", A < B)  # So sánh A có nhỏ hơn B không
print("A < C (10 < 10):", A < C)  # So sánh A có nhỏ hơn C không

print("\n=== Bước 23: Toán tử logic AND (và) ===")
print("A > 10 and B > 10 (10 > 10 and 12 > 10):", A > 10 and B > 10)  # Cả hai điều kiện phải đúng

print("\n=== Bước 24: Toán tử logic OR (hoặc) ===")
print("A > 10 or B > 10 (10 > 10 or 12 > 10):", A > 10 or B > 10)   # Chỉ cần một điều kiện đúng
