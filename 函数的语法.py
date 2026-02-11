# 多返回值
def test_return():
    return 1, "hello", True
x, y, z = test_return()
print(x)
print(y)
print(z)
# 函数的多种传参形式
def user_info(name, age, gender):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
# 位置参数： 传递的参数和定义的参数顺序及个数必须一致
user_info("小明", 20,'男')
# 关键字参数： 函数调用时可以通过键 = 值的形式传入
# （可以与位置参数混用但是位置参数必须要在关键字参数前面，但关键字参数之间不存在顺序）
user_info(name='小王', age=11, gender='女')
user_info(name='潇潇', gender='女', age=12)
user_info('甜甜', gender='女', age=9)
# 缺省参数： 也叫默认参数，在定义函数时提供默认值（默认值必须写在最后）
def user_info(name, age, gender='男'):
    print(f"姓名是：{name}, 年龄是：{age}, 性别是：{gender}")
user_info('小天', 13)
user_info('小天', 13, gender='女')
# 不定长参数：分为位置传递（形参是元组对象）和关键字传递（形参是字典对象）
# 位置不定长，用元组接收不定长数量的参数传入  （一个*号）
def user_info(*args):
    print(f"args参数的类型是：{type(args)}, 内容是：{args}")
user_info(1, 2, 3, '小明', '男孩')
# 关键字不定长，用字典接收不定长数量的参数传入   （两个**号）
def user_info(**kwargs):
    print(f"kwargs参数的类型是：{type(kwargs)}, 内容是：{kwargs}")
user_info(name='小王', age=11, gender='男', addr='北京')


# 函数作为参数传递
def compute(x, y):
    return x + y
def test_func(compute):
    result = compute(1, 2)
    print(f"compute参数类型是：{type(compute)}")
    print(result)
test_func(compute)