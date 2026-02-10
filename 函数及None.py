# 通过函数演示特殊字面量None
# 无return语句的函数返回值
def say_hi():
    print("你好呀")
result = say_hi()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容的类型是：{type(result)}")

# 主动返回None值的函数
def say_hi2():
    print("你好呀")
    return None

result = say_hi2()
print(f"主动返回None值的函数，返回的内容是：{result}")
print(f"主动返回None值的函数，返回内容的类型是：{type(result)}")

 # None用于if的判断
def check_age(age):
    # 多行注释，便于理解函数用途，可通过将鼠标悬停于调用语句的传参部分来查看注释
    """
    check_age函数可以接收一个参数，进行判断年龄是否成年的功能
    :param age: 形参age代表传入的年龄
    :return: 返回值是判断的结果
    """
    if age > 18:
        return "sucess"
    else:
        return None
result = check_age(16)
if not result:
    print(f"未成年，不可入内")

# None可以用于声名无处使内容的变量
name = None