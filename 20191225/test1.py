# -*- coding: cp936 -*-
temp = input("�������:")
YEAR = int(temp)
# if (YEAR % 4 == 0 and YEAR % 100 != 0) or (YEAR % 400 == 0 and YEAR % 3200 != 0) or YEAR % 172800 == 0:
#     print("����")
# else:
#     print("������")

if YEAR % 4 == 0 and YEAR % 100 != 0:
    print("����")
elif YEAR % 400 == 0 and YEAR % 3200 != 0:
    print("����")
elif YEAR % 172800 == 0:
    print("����")
else:
    print("������")
