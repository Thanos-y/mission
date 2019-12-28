# #  定义一个行计数器
# row = 1
# while row <= 5:
#     col = 1                              # 定义一个列计数器
#     while col <= row:
#         print('*', end='')
#         col += 1
#     print('')
#     row += 1
# row = 1
# while row < 5:
#     col = 4
#     while col >= row:
#         print('*', end='')
#         col -= 1
#     print('')
#     row += 1


# 定义一个行计数器
# row = 1
# while row <= 5:
#     # 定义一个列计数器
#     col = 5
#     # 开始循环
#     while col >= row:
#         print('*', end='_')
#         col -= 1
#     print('#')
#     row += 1


row = 1
while row <= 5:             # 行数，循环五次
    a = 1
    col = 1
    while a <= 5 - row:     # a控制每行的空格数=5-行数，例如：第一行为5-1=4个空格
        print(' ', end='')       # 不换行
        a += 1
    while col <= row:       # col控制的数量=行数
        print('*', end='')
        col += 1
    print()
    row += 1

row = 1
while row < 5:             # 行数，循环五次
    a = 1
    col = 4
    while a <= row:     # a控制每行的空格数=5-行数，例如：第一行为5-1=4个空格
        print(' ', end='')       # 不换行
        a += 1
    while col >= row:       # col控制的数量=行数
        print('*', end='')
        col -= 1
    print()
    row += 1
