# 获取距离
cost = int(input('请输入您每次乘坐公交的费用：'))
if cost == 3:
    print('小明的出行距离是：6公里(含)内')
elif cost ==4:
    print('小明的出行距离是：6公里至12公里(含)')
elif cost ==5:
    print('小明的出行距离是：12公里至22公里(含)')
elif cost ==6:
    print('小明的出行距离是：22公里至32公里(含)')
elif cost > 6:
    print('小明的出行距离是：32公里以上')
else:
    print('请输入正确的费用')
    exit()

# 不使用一卡通的总费用
cost_2 = cost*2*20
print('小明每天上班两回两次，一个月20天，不使用一卡通总计花费：{}元'.format(cost_2))

# 使用一卡通的总费用
times = 2*20
time_1 = 100 // cost + 1
time_2 = 150 // cost + 1
# print(time_1)
# print(time_2)
cost_3 = (times - time_2)
# print('小明每天上班两回两次，一个月20天，不使用一卡通总计花费：{}元'.format(cost_3))

if cost_2 > 150:
    if 150 % cost == 0:
        cost_150 = (times - 150 / cost)*cost*0.5
        if 100 % cost == 0:
            cost_100 = (150 / cost - 100 / cost) * cost*0.8
            cost_4_1 = 100 + cost_100 + cost_150
            print('小明每天上班两回两次，一个月20天，使用一卡通总计花费format(cost_4_1)：{}元'.format(cost_4_1))
        elif 100 % cost != 0:
            cost_100 = (150 / cost - time_1) * cost*0.8
            cost_4_2 = time_1*cost + cost_100 + cost_150
            print('小明每天上班两回两次，一个月20天，使用一卡通总计花费format(cost_4_2)：{}元'.format(cost_4_2))
        else:
            pass
    elif 150 % cost != 0:
        cost_150 = (times - time_2)*cost*0.5
        if 100 % cost == 0:
            cost_100 = (time_2 - 100 / cost) * cost*0.8
            cost_4_3 = 100 + cost_100 + cost_150
            # print(cost_100)
            # print(cost_150)
            print('小明每天上班两回两次，一个月20天，使用一卡通总计花费format(cost_4_3)：{}元'.format(cost_4_3))
        elif 100 % cost != 0:
            cost_100 = (time_2 - time_1) * cost*0.8
            cost_4_4 = time_1*cost + cost_100 + cost_150
            # print(time_1*cost)
            # print(cost_100)
            # print(cost_150)
            print('小明每天上班两回两次，一个月20天，使用一卡通总计花费format(cost_4_4)：{}元'.format(cost_4_4))
        else:
            pass
    else:
        pass
elif 100 < cost_2 <= 150:
    if 100 % cost == 0:
        cost_100 = (times - 100 / cost) * cost*0.8
        cost_5_1 = 100 + cost_100
        print('小明每天上班两回两次，一个月20天，使用一卡通总计花费：{}元'.format(cost_5_1))
    elif 100 % cost != 0:
        cost_100 = (times - time_1) * cost*0.8
        cost_5_2 = time_1*cost + cost_100
        print('小明每天上班两回两次，一个月20天，使用一卡通总计花费：{}元'.format(cost_5_2))
    else:
        pass
elif cost <= 100:
    cost_6 = times*cost
    print('小明每天上班两回两次，一个月20天，使用一卡通总计花费：{}元'.format(cost_6))
else:
    pass