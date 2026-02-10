# 演示在函数使用的十号，定义的变量作用域
# 演示局部变量
def test_a():
    num = 100
    print(num)

test_a()
# 出了函数体局部变量就无法使用了
# print(num)

# 演示全局变量
num = 200
def test_b():
    print(num)
def test_c():
    print(num)

test_b()
test_c()
print(num)

# 演示函数体内修改全局变量（global关键字）

num = 300
def test_d():
    # 通过global关键字将内部定义的变量设置为全局变量，与外面的num是同一个
    global num
    num = 500
    print(num)

test_d()
test_c()