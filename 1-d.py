a = int(input())
h = a // 3600
m = (a - h * 3600) // 60
# m = a % 3600 // 60
s = a % 60
# s = a - h * 3600 - m * 60
print(str(h) + ':' + str(m) + ':' + str(s))
# print(f"{h}:{m}:{s}")
