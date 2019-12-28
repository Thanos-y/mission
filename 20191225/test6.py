x = 0
while x <= 10000:
    a = x + 100
    b = x + 168
    if a**0.5 == int(a**0.5) and b**0.5 == int(b**0.5):
        print(x)
    else:
        pass
    x += 1
#
#
#

a = 98
# print(bool(int(a**0.5)))
if a**0.5 == int(a**0.5):
    print('dui')
else:
    print('cuo')
# print(int(a**(0.5)))
# print(int(a**0.5))

# n = 0
# while (n+1)**2-n*n <= 168:
#     n += 1
#
# for i in range((n+1)**2):
#     if i**0.5 == int(i**0.5) and (i+168)**0.5 == int((i+168)**0.5) and i-100 > 0:
#         print('可能存在的数是：%d' % int(i-100))
