# 列表是python中的一种数据容器 定义语法如下
#列表可以容纳2的63次方-1个元素，可以容纳不同类型元素，允许重复元素存在
# 字面量[元素1，元素2，元素3，元素4······]
# 定义变量 变量名称 = [元素1，元素2······]
# 定义空列表 变量名称 = []或变量名称 = list()
my_list = [123,"kwz",True]
print(my_list)
print(type(my_list))
# 列表可以嵌套定义
my_list2 = [[1,2,3],[4,5,6]]
print(my_list2)
print(type(my_list2))


# 列表的下标索引0~n-1
name_list = ["Tom","Frank","Lily"]
print(name_list[0])
print(name_list[1])
print(name_list[2])
# 也可以反向索引，列表中最后一个元素的索引是-1，最前面是-n
print(name_list[-1])
print(name_list[-2])
print(name_list[-3])

# 嵌套列表取出元素
my_list3 = [[1,2],[3,4]]
print(my_list3[0][0])
print(my_list3[0][1])
print(my_list3[1][0])
print(my_list3[1][1])
