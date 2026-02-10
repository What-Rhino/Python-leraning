# 元组一旦定义完成，就不可修改，定义方式如下
# 元组可以含有不同类型的元素，可以嵌套
# 若元组中嵌套一个列表则可以修改
# 定义元组字面量：(元素1，元素2，......)
# 定义元组变量： 变量名称 = (元素1，元素2，......)
# 定义空元组： 变量名称 = （）或变量名称 = tuple()

my_tuple1 = (1,"hello",True)
my_tuple2 = ()
my_tuple3 = tuple()
print(f"my_tuple1的类型是：{type(my_tuple1)},内容是：{my_tuple1}")
print(f"my_tuple2的类型是：{type(my_tuple2)},内容是：{my_tuple2}")
print(f"my_tuple3的类型是：{type(my_tuple3)},内容是：{my_tuple3}")

# 定义单个元素的元组 注意一定要在最后加一个逗号，否则是str类型的
my_tuple4 = ("hello",)
print(f"my_tuple4的类型是：{type(my_tuple4)}")

# 嵌套元组
my_tuple5 = ((1,2,3),(4,5,6))
print(f"mytuple5的类型是：{type(my_tuple5)}, 内容是:{my_tuple5}")

# 下标索引取出元素
num = my_tuple5[1][2]
print(f"从嵌套元组中取出的元素是：{num}")


# 元组的操作：index查找法
my_tuple6 = ("传智教育", "黑马程序员", "python")
index = my_tuple6.index("黑马程序员")
print(f"在元组my_tuple6中查找黑马程序员的位置是：{index}")

# 元组的操作：count统计方法
my_tuple7 = ("传智教育", "黑马程序员", "python", "python", "python")
num = my_tuple7.count("python")
print(f"在元组my_tuple7中统计python的个数为：{num}")

# 元组的操作： len统计元组元素总数
my_tuple8 = ("传智教育", "黑马程序员", "python", "python", "python")
num = len(my_tuple8)
print(f"my_tuple元组中元素的个数为：{num}")

# 用while遍历
index = 0
while index < len(my_tuple8):
    print(f"元组的元素有：{my_tuple8[index]}")
    index +=1

# 用for遍历
for element in my_tuple8:
    print(f"元组的元素为：{element}")

# 修改元组中嵌套的列表元素
my_tuple9 = (1,2,["itheima", "itcast"])
print(f"my_tuple9的内容是：{my_tuple9}")
my_tuple9[2][0] = "黑马程序员"
my_tuple9[2][1] = "传智教育"
print(f"my_tuple9的内容是：{my_tuple9}")
