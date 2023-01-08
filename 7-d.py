x, y, z = map(int, input().split())

lst = []
for i in range(x):
    lst.append(list(map(int, input().split())))

lst2 = []
for i in range(y):
    lst2.append(list(map(int, input().split())))

result = [[0 for j in range(z)] for i in range(x)]
for i in range(x):
    for j in range(z):
        for k in range(y):
            result[i][j] += lst[i][k] * lst2[k][j]

# 複数行の出力には内包表記使うと良い
[print(*result[i]) for i in range(x)]
