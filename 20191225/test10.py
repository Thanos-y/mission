for g in range(1, 100):
    for m in range(1, 100):
        for j in range(1, 100):
            sum1 = int(g)*15 + int(m)*9 + int(j)
            sum2 = int(g) + int(m) + int(j)
            if int(sum1) == 300 and int(sum2) == 100:
                print("公鸡{}只，母鸡{}只，小鸡{}只".format(g, m, j))
else:
    print("完")
