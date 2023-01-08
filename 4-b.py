import math

r = float(input())

# 解1
print(f"{math.pi * r ** 2:.6f} {2 * r * math.pi:.6f}")

# 解2
s = math.pi * r**2
length = 2 * r * math.pi
print(s, length)
