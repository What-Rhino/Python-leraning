# 语法一 ：range(num) 获取一个从0开始到num结束的数字序列，
# 不包含num本身，如range（5）获得0 1 2 3 4
x = 2# 这里定义的x和循环里的变量x不是一个
for x in range(10):
    print(x)
print(x)# 如果想使用临时变量，需要在之前就定义
# 语法二： range（num1，num2） 获得一个从num1开始到num2结束的数字序列，
# 不包含num2本身，如range（5，10）获得5 6 7 8 9
for x in range(5,10):
    print(x)

#语法三： range（num1，num2，step） 获得一个从num1开始，到num2结束的数字序列，
# 不包含num2本身，步长为step如range（5，10，2）获得5 7 9
for x in range(5,10,2):
    print(x)