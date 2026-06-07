'''
Bài toán Gà Chó: Có 12 con vừa gà vừa chó và có 30 cái chân. Hỏi có bao nhiêu gà?

LỜI GIẢI:

Giả sử tất cả số con đều là chó, vậy số chân sẽ là:
12 x 4 = 48 chân 

Theo bài ra, tổng số chân chỉ là 30 nên số chân dư ra là:
48 - 30 = 18 chân 

Nếu ta thay mỗi chú chó bằng 1 số chú gà thì sẽ giảm được 2 chân. 
Vậy để giảm được 18 chân số con gà sẽ là:
18: 2 = 9 con
'''

# Tổng số con vật (gà + chó)
total_animals = 12
# Tổng số chân đếm được
total_legs = 30
# Giả sử tất cả đều là chó: mỗi chó có 4 chân
all_dogs = total_animals * 4
# Tính số chân dư so với thực tế
extra_legs = all_dogs - total_legs
# Mỗi con gà có 2 chân, nên chia số chân dư cho 2 ra số con gà
chickens = extra_legs // 2
# In kết quả: 9 con gà
print(chickens)
