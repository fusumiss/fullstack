print("this is my first program")

# 循环
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# for i in range(1, 101, 2):  # 第三个参数：  是 步长
#     print(i)

a = ['zhangsan', 'lisi', 'wangwu']

# a.append('doubi')
# a.insert(1, 'zhaoliu')

a[1:3] = ['a','b']
a.remove('zhangsan') # 删除的里面只能是值，不能是下标
a.sort(reverse=True)

range(10)
print(a)
