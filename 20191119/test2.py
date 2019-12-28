# 方法一输出
# input收录信息
name = input("请输入你的姓名：")
qq = input("请输入你的QQ号：")
cell = input("请输入你的手机号：")
address = input("请输入你的地址：")
print("==================================")
print("姓名：%s\nQQ：%s\n手机号：%s\n地址：%s" % (name, qq, cell, address))  # %s占位符需在同一个""内
print("==================================")

# # 方法二输出
# # input收录信息
name = input("请输入你的姓名：")
QQ = input("请输入你的QQ号：")
Moblie = input("请输入你的手机号：")
address = input("请输入你的地址：")
# 打印收录信息类型
# print(type(name))
# print(type(QQ))
# print(type(Moblie))
# print(type(address))
# 定义输出变量
strNiu = "姓名：{}\nQQ：{}\n手机号：{}\n地址：{}".format(name, QQ, Moblie, address)
# print(type(strNiu))
print("==================================")
print(strNiu)
print("姓名：{}\nQQ：{}\n手机号：{}\n地址：{}".format(name, QQ, Moblie, address))
print("==================================")

# 方法三输出
# input收录信息
name = input("请输入你的姓名：")
QQ = input("请输入你的QQ号：")
mobile = input("请输入你的手机号：")
address = input("请输入你的地址：")
# format填入信息
str1 = "姓名：{}".format(name)
str2 = " QQ ：{}".format(QQ)
str3 = "手机：{}".format(mobile)
str4 = "地址：{}".format(address)
# print输出信息
print("==================================")
print(str1, str2, str3, str4, sep="\n")
print("==================================")
