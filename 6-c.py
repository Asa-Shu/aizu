n = int(input())
arr3d = [[[0 for k in range(10)] for j in range(3)] for i in range(4)]
for i in range(n):
    b, f, r, v = map(int, input().split())
    arr3d[b - 1][f - 1][r - 1] += v

for i in range(4):
    for j in range(3):
        for k in range(10):
            print(" " + str(arr3d[i][j][k]), end="")
        print()
    if i != 3:
        print("#" * 20)
