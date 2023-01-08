n, m = map(int, input().split())

lst = []
lst2 = []
for i in range(n):
    lst.append(list(map(int, input().split())))
for j in range(m):
    lst2.append(int(input()))

result = []
for i in range(n):
    s = 0
    for j in range(m):
        s += lst[i][j] * lst2[j]
    result.append(s)
    print(result[i])

# numpyを使ったコード

# import numpy as np
# n, m = map(int, input().split())

# arr = []
# for i in range(n):
#     arr.append(list(map(int, input().split())))
# arr = np.array(arr)
# arr2 = []
# for j in range(m):
#     arr2.append(int(input()))
# arr2 = np.array(arr2)

# result = arr @ arr2
# for i in range(n):
#     print(result[i])
