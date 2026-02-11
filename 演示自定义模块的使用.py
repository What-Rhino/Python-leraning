"""
# 如果两个模块遇到同名函数，先调用的会被覆盖
# 用import导入整个模块
import my_model1
my_model1.test(1, 2)
"""
# 导入函数
# 如果两个模块遇到同名函数，先调用的会被覆盖
from my_model1 import test
from my_model2 import test
test(1,2)

#__all__的使用
# 在模块程序中，通过定义all变量，来决定通过*方法调用时能使用的函数
from my_model2 import *
test(1,2)
# test2(1,2) 由于all的限制 test2不能通过*导入

