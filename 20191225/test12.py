import random
i = random.randint(1, 21)
j = int(input('请输入猜数次数：'))
g = 1
for g in range(1, j+1):
    n = int(input('请输入你猜的数：'))
    if n > i:
        print('你猜大了!')
    elif n < i:
        print('你猜小了!')
    else:
        print('恭喜你猜对了!')
        print('游戏结束')
        exit()
    g += 1
print('游戏结束')