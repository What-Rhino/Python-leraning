my_list = ["itcast", "itheima", "python"]
# 1.1查找元素在列表内的下标索引
index = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")
# 1.2如果被查找的元素不存在，会报错
"""index = my_list.index("hello")
print(f"itheima在列表中的下标索引值是：{index}")
"""
# 2.修改特定下标索引的值
my_list[0] = "kwz"
print(f"列表被修改元素值后，结果是：{my_list}")

# 3.在指定下标位置插入新元素
my_list.insert(1,"best")# 第一个是要插入的位置
print(f"插入后，列表变为：{my_list}")

# 4.在列表尾部插入“单个”新元素
my_list.append("handsome")
print(f"尾部追加一个元素后，列表变为：{my_list}")

# 5.在列表的尾部追加“一批”新元素
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(f"尾部追加一个新列表后，列表变为：{my_list}")

# 6.删除指定下表索引的元素（两种方式）
my_list = ["itcast", "itheima", "python"]# 复原列表
# 6.1 方式1：del 列表[下标]
del my_list[2]
print(f"列表删除元素后的结果是：{my_list}")
# 6.2 方式2：通过pop取出，列表.pop()下标
my_list = ["itcast", "itheima", "python"]
element = my_list.pop(2)
print(f"通过pop方法取出后列表的结果是：{my_list}，取出的元素是：{element}")

# 7.删除某元素在列表中的“第一个”匹配项
my_list = ["itcast", "itheima", "itheima","python"]
my_list.remove("itheima")
print(f"通过remove方法移除元素后的结果是：{my_list}")

# 8.清空列表
my_list.clear()
print(f"列表被清空了，结果是：{my_list}")

# 9.统计列表内某元素的数量
my_list = ["itcast", "itheima", "itheima","python"]
count = my_list.count("itheima")
print(f"列表中itheima的数量是：{count}")

# 10.统计列表中全部元素数量
my_list = ["itcast", "itheima","itcast", "itheima","python"]
count = len(my_list)
print(f"列表中的元素数量总共有：{count}个")