a = 2**10                # + - * / % //
print(a)
print(bin(a))

b = 126
c = ~128
print(bin(b))
print(bin(c))
#
# val = b >> 2
# print(bin(val))
#
# val_2 = b << 2
# print(bin(val_2))

# val_3 = 11 & 12
# print(bin(11))
# print(bin(12))
# print(bin(val_3))

# val_3 = 11 | 12
# print(bin(11))
# print(bin(12))
# print(bin(val_3))

# val_3 = 11 ^ 12
# print(bin(11))
# print(bin(12))
# print(bin(val_3))

print(a >= 1024)                # <= > < == !=

b += a                          # -= *= /= %= //= **= =
print(b)

d = b
print(d is b)                     # is not

e = [1, 2, 4]
f = 3
print(f not in e)                 # in

print(a and b)
print(a or b)
print(b or a)

g = False
print(not g)

