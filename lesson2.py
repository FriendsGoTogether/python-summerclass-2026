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

total_animals = 12
total_legs = 30
all_dogs = total_animals * 4
extra_legs = all_dogs - total_legs
chickens = extra_legs // 2
print(chickens)

