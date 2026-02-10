# while循环实现
print(f"用while循环实现：\n")
i = 1
while i <= 9:
    j=1
    while j <= i:
        print(f"{j}*{i} = {j*i}\t", end = ' ')
        j = j+1
    print(f"\n")
    i = i+1
# for循环实现
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i} = {j*i}\t",end = ' ')
    print("\n")