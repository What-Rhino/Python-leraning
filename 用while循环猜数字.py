import random
num = random.randint(1, 100)
i = 1
guess_num = int(input(f"请输入第{i}次猜测的数字："))
while(guess_num != num):
    i += 1
    if guess_num > num:
        print("你猜的数字偏大，请再猜一次")
        guess_num = int(input(f"请输入第{i}次猜测的数字："))

    else:
        print("你猜的数字偏小，请再猜一次")
        guess_num = int(input(f"请输入第{i}次猜测的数字："))

print(f"恭喜你！", end=' ')
print(f"你在第{i}次猜对啦！")