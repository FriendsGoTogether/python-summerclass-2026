'''
Bài toán Gà Chó: Có 12 con vừa gà vừa chó và có 30 cái chân. Hỏi có bao nhiêu gà?

LỜI GIẢI:

Ta xét lần lượt số gà là 1, 2, 3,...12 rồi tính số chân tương ứng. 
Khi nào số chân bằng 30 thì ta sẽ tìm được số gà cần tìm.

'''
for chickens in range(12):
    dogs = 12 - chickens
    if chickens * 2 + dogs * 4 == 30:
        print(chickens)
        break
