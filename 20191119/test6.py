# input收录房屋长宽信息
length = input("房屋长度（m）：")
width = input("房屋宽度（m）：")
# 计算房屋面积及周长
acreage = (int(length)*int(width))
perimeter = (int(length)*2+int(width)*2)
# 定义返回变量
str1 = "房屋面积：{}平方米".format(acreage)
str2 = "房屋周长：{}米".format(perimeter)
# 输出结果
print(str1, str2, sep="\n")
