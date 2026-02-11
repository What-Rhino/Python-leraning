"""
def关键字可以定义带名称的函数
lambda关键字定义无名称的函数
无名称的函数只能临时使用一次。定义语法如下：
lambda 传入参数：函数体（只能写一行代码）
"""
def test_func(compute):
    result = compute(1, 2)
    print(result)
# 通过匿名函数lambda的形式，传入函数参数
test_func(lambda x, y:x+y )