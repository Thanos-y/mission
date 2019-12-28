# 设置已保存的id和pw
id_Save = "ace"
pw_Save = "1234"

# input收录新输入id和pw信息
id_Input = input("ID:")
pw_Input = input("PassWord:")
# 比对新输入和以保存信息
if (id_Input == id_Save) and (pw_Input == pw_Save):  # id和pw同时验证正确
    print("welcome back")
else:                                                         # id或pw错误一个以上
    print("Incorrect username or password")
