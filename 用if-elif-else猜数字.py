import random
num = random.randint(1,10)# 产生从1到10的整数随机数
guess_num = int(input("请输入你要猜测的数字："))
if guess_num == num:
    print("恭喜，第一次就猜中了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")
    guess_num = int(input("再次输入你要猜测的数字："))
    if guess_num == num:
        print("第二次就猜中了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")
        guess_num = int(input("第三次输入你猜测的数字："))
        if guess_num == num:
            print("第三次猜中了")
        else:
            print("三次机会用完了，你没有猜中")
            print(f"正确数字是：{num}")