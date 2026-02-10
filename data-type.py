# 方式1：使用print直接输出类型信息
print(type("康维哲"))
print(type(666))
print(type(3.141))
# 方式2：使用变量存储type()语句的结果，并输出
string_type = type("康维哲")
int_type = type(666)
float_type = type(3.141)
print(string_type)
print(int_type)
print(float_type)
# 方式3： 使用type()语句，查看变量中存储的数据类型信息
name = "康维哲"
print(type(name))
"""变量是没有类型的，只是变量中存储的数据是有类型的
通过type()查看的是变量中存储数据的类型而不是变量本身的数据类型"""