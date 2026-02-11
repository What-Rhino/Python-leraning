# 模块的导入方式 语法如下：
# [from 模块名] import [模块 | 类 | 变量 | 函数 |*]  [as别名]
# 用import引入整个time模块
"""
import time # 导入Python内置的time模块(time.py这个代码文件)
print("你好")
time.sleep(5) # 通过.使用模块内的全部功能(类、函数、变量)
print("我好")
"""

# 用from-import导入time中的sleep功能(函数)

from time import sleep
print("你好")
sleep(6)
print("我好")

# 使用*导入time的全部功能
from time import *
print("你好")
sleep(6)
print("我好")

#设置导入模块或功能的别名as

#模块别名

import time as t
print("你好")
t.sleep(6)
print("我好")

#功能（函数）别名

from time import sleep as sl
print("你好")
sl(6)
print("我好")
