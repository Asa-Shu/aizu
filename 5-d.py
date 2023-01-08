n = int(input())
for i in range(1, n + 1):
    if i % 3 == 0:
        print(f" {i}", end="")
    else:
        j = i
        while j > 0:
            if j % 10 == 3:
                print(f" {i}", end="")
                break
            else:
                j //= 10

# 別解
for i in range(1, n + 1):
    if i % 3 == 0 or "3" in str(i):
        print(f" {i}", end="")
