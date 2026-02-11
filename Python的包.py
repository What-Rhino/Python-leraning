"""
演示python中的包
"""
# 创建一个包
# 导入自定义的包中的模块，并使用

# 通过import
if(False):
    import My_Package.my_model1
    import My_Package.my_model2
    My_Package.my_model1.info_print1()
    My_Package.my_model2.info_print2()

# 通过from-import
if(False):
    from My_Package import my_model1
    from My_Package import my_model2
    my_model1.info_print1()
    my_model2.info_print2()

# 直接导入具体功能
if(True):
    from My_Package.my_model1 import info_print1
    from My_Package.my_model2 import info_print2
    info_print1()
    info_print2()

# 演示通过init文件中的__all__变量控制调用的模块，需要与*方法搭配

from My_Package import *
# my_model2.info_print2()
my_model1.info_print1()
