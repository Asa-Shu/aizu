import math

# 実数で与えられるのでfloat型
x, y, z, w = map(float, input().split())

print(math.sqrt((x - z)**2 + (y - w)**2))  # mathをimportしないで**(1/2)にしても良い
