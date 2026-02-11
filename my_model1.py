__all__ = ['test']
def test (a, b):
    print(a+b)

def test2 (a, b):
    print(a-b)
#通过main功能满足可以在模块内部测试函数，也满足在引入模块时不会自动调用
if __name__ == '__main__':
    test(1,2)