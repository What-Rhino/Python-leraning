# 将数字类型转换成字符串
num_str = str(16)
print(type(num_str), num_str)
# 将浮点数类型转换成字符串
float_str = str(3.1415)
print(type(float_str), float_str)
# 将字符串转换成数字
num = int("11")
print(type(num), num)

num2 = float("3.1415")
print(type(num2), num2)

# num3 = int("康维哲")
# print(type(num3), num3)
# num 4 = int("3.141")也是错误的
"""任何数据类型都能转换成字符串类型
但并不是所有的字符串都能传换成数字或其他数据类型"""
# 整数转浮点数
float_num = float(111)
print(type(float_num),float_num)
# 浮点数转整数(会丢失精度)
int_num = int(3.141)
print(type(int_num), int_num)

