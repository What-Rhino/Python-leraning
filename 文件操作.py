# 演示文件的读取
import time

# 打开文件
# 格式：文件路径：/名称，"操作方法"， 编码格式
# r表示只读
f = open("D:/测试.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件 - read方法 文件名.read(num)num代表读取字节，不填则读取全部
print(f"读取10个字节的结果是：{f.read(10)}")
# 连续调用两次read会从上一次read的结尾处继续读取
print(f"读取全部内容的结果是：{f.read()}")
print("---------------------------------------------")

# 读取文件 - readlines()读取文件的全部行，封装到一个列表中
f = open("D:/测试.txt", "r", encoding="UTF-8")
lines = f.readlines()
print(f"lines的对象类型是：{type(lines)}")
print(f"lines对象的内容是：{lines}")

# 一次读取一行readline()方法
f = open("D:/测试.txt", "r", encoding="UTF-8")
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(f"第一行数据是：{line1}")
print(f"第二行数据是：{line2}")
print(f"第三行数据是：{line3}")

# for循环读取文件
f = open("D:/测试.txt", "r", encoding="UTF-8")
for line in f:
    print(f"每一行的数据是：{line}")

#文件的关闭 文件名.close()
# 将程序停止在此处500秒，会一直占用该文件，导致无法修改文件
# time.sleep(500)
f.close()

# with open语法操作 可以自动关闭文件 防止忘记
with open("D:/测试.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一行的数据是：{line}")

# time.sleep(5000)

# 文件的写入操作
#打开文件 用w写的模式
# 当文件不存在的时候 w会把文件创建出来 再写入
f = open("D:/测试2.txt", "w", encoding="UTF-8")
# write会将内容写入缓冲区，当调用flush时才会一起传入硬盘
f.write("hello world")
# time.sleep(5000)
# flush刷新文件
f.flush()
# print(f"测试2.txt的内容是：{f.read()}")
# 用close关闭，是内置flush的，就不用close了

#当文件存在时，会把原本的全部清空再写入
f = open("D:/测试.txt", "w", encoding="UTF-8")
f.write("黑马程序员")
f.close()
print("------------------------------------------")

# 追加写入用a模式，如果文件存在，则在最后追加，如果不存在则创建文件
f = open("D:/测试.txt", "a", encoding="UTF-8")
f.write("学python的最佳选择")
f.write("\n黑马程序员")
f.flush()

# 对于不存在的文件
f = open("D:/测试3.txt", "a", encoding = "UTF-8")
f.write("测试不存在的文件追加写入")
f.flush()
print(f"测试3写入的内容是：{f.read()}")





