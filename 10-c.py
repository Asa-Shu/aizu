import math

while 1:
    n = int(input())
    if n == 0:
        break
    lst = list(map(float, input().split()))
    ave = sum(lst) / n
    V = 0
    for i in range(n):
        V += (lst[i] - ave)**2
    V /= n
    print(math.sqrt(V))
