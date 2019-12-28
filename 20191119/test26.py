
import time

time01 = time.time()       # 起始时刻
a = ""
for i in range(2000000):
    a += "sxt"
time02 = time.time()       # 结束时刻

print("\"+\"运行时间："+str(time02-time01))


time03 = time.time()        # 起始时刻
li = []
for i in range(2000000):
    li.append("sxt")
a = "".join(li)
time04 = time.time()       # 结束时刻

print("\"join\"运行时间："+str(time04-time03))
