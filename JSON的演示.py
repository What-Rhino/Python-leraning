"""
演示JSON数据和Python字典的相互转换 dumps和loads
"""

import json

# 准备列表，列表内的每一个元素都是字典，将其转换为JSON
data = [{"name": "张大山", "age": 11},{"name": "王大锤", "age": 13},{"name": "赵小虎", "age":16}]
# 如果想要展示出json码里的中文，就需要写ensure_ascii=False,表示不用ascii码转换，如果不写，展示出的会是一串代码
json_str = json.dumps(data, ensure_ascii=False)
print(f"json_str的类型是：{type(json_str)}")
print(json_str)

# 准备字典，将字典转换为Json
d = {"name": "周杰伦", "addr": "台北"}
json_str = json.dumps(d,ensure_ascii=False)
print(f"json_str的类型是：{type(json_str)}")
print(f"json_str的内容是：{json_str}")

# 将JSON字符串转化为字典的列表
s = '[{"name": "张大山","age": 11}, {"name": "王大锤", "age": 13},{"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(f"l的类型是：{type(l)}")
print(f"l的内容是：{l}")

# 将JSON字符串转化为字典
s = '{"name": "周杰伦", "addr": "台北"}'
d = json.loads(s)
print(f"d的类型是：{type(d)}")
print(f"d的内容是：{d}")

