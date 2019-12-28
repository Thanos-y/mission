str1 = input("请输入字符串：")
alpha = 0
digit = 0
space = 0
other = 0
for i in str1:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        digit += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print("字母有{}个，数字有{}个，空格有{}个，其他字符有{}个。".format(alpha, digit, space, other))
