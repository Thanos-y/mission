# 欢迎语
print("欢迎使用Thanosy的简易加法计算器")
# input收录计算数
a = input("请输入你要计算的第一个数:")
b = input("请输入你要计算的第二个数:")
# 计算方法固定为"+"
int_1 = (int(a) + int(b))   # 整数计算需定义类型
int_2 = (a + b)            # 为int定义，自动定义为str
print("计算结果是：", int(int_1))  # 数字加法结果
print("计算结果是：", int(int_2))  # 字符相加结果
# 打印结果类型
print(type(int_1))
print(type(int_2))
