# 字典定义同样使用{}，但是存储的元素是键值对，语法如下：
# 字典的key不可以重复，不可以使用下标索引，要通过key找value
# key（除了不可以是字典以外）和value可以是任何类型
# 定义字典字面量: {key:value, key:value, ......}
# 定义字典变量: my_dict = {key:value, key:value, ......,}
# 定义空字典： my_dict = {}或 my_dict = dict()

# 定义字典
my_dict1 = {"王力鸿": 99, "周杰轮": 88, "林俊节": 77}
# 定义空字典
my_dict2 = {}
my_dict3 = dict()
print(f"字典1的内容是：{my_dict1},类型：{type(my_dict1)}")
print(f"字典2的内容是：{my_dict2},类型：{type(my_dict2)}")
print(f"字典3的内容是：{my_dict3},类型：{type(my_dict3)}")

# 从字典中基于key获得value
my_dict1 = {"王力鸿":99, "周杰轮":88, "林俊节":77}
score = my_dict1["王力鸿"]
print(f"王力鸿的考试分数是：{score}")

# 字典的嵌套定义
stu_score_dict = {
    "王力鸿": {
        "语文": 77,
        "数学": 66,
        "英语": 33
    }, "周杰伦": {
        "语文": 88,
        "数学": 86,
        "英语": 55
    }, "林俊杰": {
        "语文": 99,
        "数学": 96,
        "英语": 66
    }
}
print(f"学生的考试信息是：{stu_score_dict}")

# 从嵌套的字典中获取信息
score = stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文信息是：{score}")
