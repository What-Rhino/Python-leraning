# 序列是指：内容连续，有序，可使用下表索引的一类数据容器
# 列表，元组，字符串都可视为序列

# 切片操作(可以正向也可以反向)：从一个序列中取出一个子序列（不会影响本身，会得到一个新的序列）
# 语法： 序列[起始下标：结束下标：步长]
# 起始下标(包含起点)留空表示从头开始，结束下标（不包含起点）留空表示截取到结尾
# 步长1表示挨个取，步长2表示隔一个一取,(步长默认为1，可以省略)


# 对list切片
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4]
print(f"结果1：{result1}")

# 对turple切片
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]
print(f"结果2：{result2}")

# 对string进行切片
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3：{result3}")

# 对string负向切片
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果4：{result4}")# 等同于将序列反转

# 对列表进行负向切片
my_list = [0, 1, 2, 3, 4, 5, 6]
result5 = my_list[3:1:-1]
print(f"结果5：{result5}")# 等同于将序列反转

# 对元组进行负向切片
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result6 = my_tuple[::-2]
print(f"结果6：{result6}")# 等同于将序列反转