a, b, c = map(int, input().split())
count = 0
for i in range(a, b + 1):  # a 以上 b + 1 未満
    if c % i == 0:
        count += 1
print(count)
