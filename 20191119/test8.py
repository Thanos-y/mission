print("欢迎来到Thanosy's 计算器！")
x = input("请选择您要计算的方法：")                # 先判断exit退出
if x == "exit":                                              # 判定只能用==，不能用is
    print('欢迎下次光临！')
    exit()
else:                                                         # 非退出，进行运算判定
    a = input("请输入您要计算的第一个数：")
    b = input("请输入您要计算的第二个数：")
    if x is "+":                                             # +号判断可以用is
        c = int(a) + int(b)
    elif x is "-":                                            # -号判断可以用is
        c = int(a) - int(b)
    elif x is "*":                                            # *号判断可以用is
        c = int(a) * int(b)
    elif x is "/":                                             # /号判断可以用is，但计算结果为float？
        c = int(a) / int(b)
    elif x is "%":                                           # %号判断可以用is
        c = int(a) % int(b)
    elif x == "//":                                           # //号判断不可以用is，只能用==
        c = int(a) // int(b)
    elif x == "**":                                          # **号判断不可以用is，只能用==
        c = int(a) ** int(b)
    else:                                                     # x输入其他字符，返回none
        c = None
    print(c)
    print(type(c))
    print('==========')
