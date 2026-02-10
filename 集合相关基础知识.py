# 不支持重复元素且内容无序(所以集合不是序列), 所以不支持下标访问，但允许修改
# 定义集合字面量 {元素1，元素2......}
# 定义集合变量 变量名称 = {元素，元素，......}
# 定义空集合 变量名称 = set()（注：不能用变量名称 = {}定义空集合，因为这样会定义一个空字典）

# 定义集合
my_set = {"传智教育", "黑马程序员", "itheima", "传智教育", "黑马程序员", "itheima"}
my_set_empty = set()
print(f"my_set的内容是：{my_set}，类型是： {type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")

# 添加新元素
my_set.add("python")
my_set.add("传智教育")
print(f"my_set添加元素后的结果是：{my_set}")
# 移除元素
my_set.remove("黑马程序员")
print(f"my_set移除黑马程序员后的结果是：{my_set}")

# 随机取出一个元素
my_set = {"传智教育", "黑马程序员", "itheima"}
element = my_set.pop()
print(f"集合被取出的元素是：{element}，取出元素后my_set：{my_set}")

# 清空集合
my_set.clear()
print(f"集合被清空了，结果是：{my_set}")

# 取出两个集合的差集： 集合1.difference(集合2)（取出集合1有集合2没有的）
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.difference(set2)
print(f"取出差集后的结果是：{set3}")
print(f"取出差集后，原set1的内容是：{set1}")
print(f"取出差集后，原set2的内容是：{set2}")

# 消除2个集合的差集 ： 集合1.difference_update(集合2)（删除集合1中和2相同的元素）
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)
print(f"消除差集后，原set1的内容是：{set1}")
print(f"消除差集后，原set2的内容是：{set2}")

# 两个集合合并 ：集合1.union(集合2) （将集合1和集合2合并）
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"合并后的结果是：{set3}")
print(f"合并后，原set1的内容是：{set1}")
print(f"合并后，原set2的内容是：{set2}")

# 统计元素数量len（）注意会去重
set1 = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
num = len(set1)
print(f"集合中元素数量有：{num}个")
# 集合的遍历（集合不支持下标，所以不能用while）
set1 = {1, 2, 3, 4, 5}
for element in set1:
    print(f"集合的元素有：{element}")