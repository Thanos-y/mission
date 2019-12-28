# str[start从哪个数开始: end数几个数: feet步长]
# -3 = 7-10
str = '0123456789'
print(str[0:3])  # 012
print(str[:])  # 0123456789
print(str[6:])  # 6789
print(str[:-3])  # [:7] 0123456
print(str[2])   # 02468 error
print(str[-1])  # 9876543210 error
print(str[::-1])  # 9876543210
print(str[-3:-1])  # 78
print(str[-3:])  # 789
print(str[-5:-3])  # 56


Str = '1a'
print(Str.isalnum())
Str = 'a'
print(Str.isalpha())
Str = '1'
print(Str.isdigit())
Str = ' '
print(Str.isspace())
Str = 'a'
print(Str.islower())
Str = 'A'
print(Str.isupper())
Str = 'Big'
print(Str.istitle())


str = " I love you "
print(str.strip())
print(str.lstrip())
print(str.rstrip())


name = "thanosy"
print(name.count('o'))
print(name.capitalize())
print(name.find('o'))
print(name.index('o'))
print(name.replace('o', 'ou'))
age = 17
print("thanosy is {}".format(age))

str6 = "a b c"
split_a = str6.split()
print(split_a)

str7 = "a,b,c"
split_b = str7.split(",")
print(split_b)

str8 = "*".join(split_b)
print(str8)

code = "vivi-sun, yiyi-yang, yoyo-jang"
print(code.split(","))
print("_love_".join(["vivi-sun", "yiyi-yang"]))
