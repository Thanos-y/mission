# num = input("请问你想抽奖多少次：")
# num = int(num)
# for i in range(num):
#     print("抽第%d次" % (i+1))
#     print("抽第{}次".format(i+1))
# print("抽奖完毕，祝您好运。")


# for i in range(1, 10):
#     for j in range(1, i+1):
#         a = i*j
#         print("{}*{}={}\t".format(i, j, a), end="")
#     print()


# for i in range(1, 10):
#     for j in range(1,i+1):
#         print("%d*%d=%d\t"%(j,i,i*j),end="")
#     print()


# a = 1
# count = 1
# while count < 100:
#     a += 1
#     print(a)
#     count += 1
#     print(a + a)


# sum = 0
# count = 1
# while count < 101:
#     sum += count
#     count += 1
# print(sum)

# for i in range(1, 101):
#     # j j = i+1
#     # sum1 = i +
#     # sum += int(sum1)
#     sum = 0
#     sum += i
# sum += sum
# print(su)


# sum = 0
# for i in range(1, 101):
#     sum += i
# print(sum)


# play = input("欢迎参加幸运大抽奖，请问您要抽几次：")
# count = 1
# while count < int(play)+1:
#     if count == 7:
#         print("恭喜你抽中大奖")
#         count += 1
#         continue
#     print("第{}次".format(count))
#     count += 1
# print("抽奖结束")


# play = input("欢迎参加幸运大抽奖，请问您要抽几次：")
# count = 1
# while count < int(play)+1:
#     if count == 7:
#         print("恭喜你抽中大奖")
#         count += 1
#         break
#     print("第{}次".format(count))
#     count += 1
# print("抽奖结束")


# count = 1
# while count < 11:
#     if count == 6:
#         print("不合格")
#         count += 1
#         continue
#     print("合格")
#     count += 1


# num = int(input("今天要吃几个包子？"))
# for i in range(1, num+1):
#     if i == 11:
#         break
#     print("第{}个".format(i))
# else:
#     print("吃完了，好饱")
# print("over")


# for b in range(1, 10):
#     for s in range(1, 10):
#         for g in range(1, 10):
#             sum1 = int(b)*100 + int(s)*10 + int(g)
#             sum2 = b**3 + s**3 + g**3
#             if sum1 == sum2:
#                 print("百位数为：{}，十位数为：{}，个位数为；{}".format(b, s, g))
# # else:
# #     print("none")


for g in range(1, 100):
    for m in range(1, 100):
        for j in range(1, 100):
            sum1 = int(g)*15 + int(m)*9 + int(j)
            sum2 = int(g) + int(m) + int(j)
            if int(sum1) == 300 and int(sum2) == 100:
                print("公鸡{}只，母鸡{}只，小鸡{}只".format(g, m, j))
else:
    print("完")
