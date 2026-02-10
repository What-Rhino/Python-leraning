# 1、用print函数输出提示信息
print("请输入你的姓名")
name = input()
print("你的姓名是： " + name)
# 2、用input函数输出提示信息
name = input("请告诉我你的名字")
print("我知道了，你的名字是：%s" % name)
# 默认input传入的类型是字符串类型
num = input("请输入你的学号")
print("你的学号的数据类型是：" % type(num))