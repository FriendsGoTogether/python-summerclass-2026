'''
Bài toán Gà Chó: Có 12 con vừa gà vừa chó và có 30 cái chân. Hỏi có bao nhiêu gà?

LỜI GIẢI:

Ta xét lần lượt số gà là 1, 2, 3,...12 rồi tính số chân tương ứng. 
Khi nào số chân bằng 30 thì ta sẽ tìm được số gà cần tìm.

'''

# Duyệt qua các giá trị có thể của số gà từ 1 đến 12
for chickens in range(1, 13):
    # Số chó bằng tổng số con trừ số gà hiện tại
    dogs = 12 - chickens
    # Kiểm tra nếu tổng số chân (gà có 2 chân, chó có 4 chân) bằng 30
    if chickens * 2 + dogs * 4 == 30:
        # In ra số gà đúng khi tìm thấy
        print(chickens)
        # Thoát vòng lặp ngay khi tìm được kết quả
        break
