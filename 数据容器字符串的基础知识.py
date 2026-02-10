# 字符串也不支持修改
my_str = "itheima and itcast"
# 通过索引下标取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}中取下标为2的元素，值是：{value}")
print(f"从字符串{my_str}中取下标为-16的元素，值是：{value2}")


#字符串常用操作：
#index方法：
value = my_str.index("and")
print(f"在字符串中查找and，其起始下标是：{value}")

# 字符串的替换 replace ,因为字符串不可修改，所以本质上是得到了一个新的字符串
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str},替换后得到：{new_my_str}")

# 字符串的分割 split, 按照指定分隔字符串，划分成多个字符串，得到一个列表对象
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list},类型是：{type(my_str_list)}")

# 字符串的规整操作 strip, 去除前后空格（或指定字符串）
my_str = "  hello python itheima itcast  "
new_my_str = my_str.strip()# 不传入参数 去除首尾空格
print(f"字符串{my_str}被strip后变为：{new_my_str}")

my_str = "12hello python itheima itcast21"
new_my_str = my_str.strip("12")# 去除字符串1和字符串2
print(f"字符串{my_str}被strip（“12）后变为：{new_my_str}")

# 统计字符串中某字符串出现的次数 count
my_str = "hello python itheima itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")

# 统计字符串长度 len
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")