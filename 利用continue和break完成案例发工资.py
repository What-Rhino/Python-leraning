money = 10000
for i in range(1, 21):# 从1遍历到20
    import random
    score = random.randint(1, 10)

    if score < 5:
        print(f"员工{i}的绩效分{score}，不满足，下一位")
        continue# continue跳过一次循环
    elif money >= 1000:
        money -= 1000
        print(f"员工{i}发放工资1000，工资账户余额：{money}")
    elif money < 1000:
        print(f"余额不足，当前余额：{money}元，不足以发工资，不发了")
        break