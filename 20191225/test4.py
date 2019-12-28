str1 = "hello world god is always busy"
h = 0
e = 0
l = 0
o = 0
w = 0
r = 0
d = 0
i = 0
s = 0
a = 0
y = 0
b = 0
u = 0
g = 0
n = 0
for q in str1:
    if q == "h":
        h += 1
    elif q == "e":
        e += 1
    elif q == "l":
        l += 1
    elif q == "o":
        o += 1
    elif q == "w":
        w += 1
    elif q == "r":
        r += 1
    elif q == "d":
        d += 1
    elif q == "i":
        i += 1
    elif q == "s":
        s += 1
    elif q == "a":
        a += 1
    elif q == "y":
        y += 1
    elif q == "b":
        b += 1
    elif q == "u":
        u += 1
    elif q == "g":
        g += 1
    else:
        n += 1
print("h = {}, e = {}, l = {}, o = {}, w = {}, r = {}, d = {}, i = {}, s = {}, a = {}, y = {}, b = {} , \
u = {} , g = {}, n = {}".format(h, e, l, o, w, r, d, i, s, a, y, b, u, g, n))
