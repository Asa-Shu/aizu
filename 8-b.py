while True:
    x = input()
    if x == "0":
        break
    a = list(map(int, x))
    print(sum(a))

# 別解
while True:
    x = int(input())
    lst = []
    if x == 0:
        break
    while x >= 10:  # 下のコードのx >= 1 を使う方が良い汎用性高い
        lst.append(x % 10)
        x //= 10
    lst.append(x)
    print(sum(lst))

# 別解
while True:
    x = int(input())
    sum = 0
    if x == 0:
        break
    while x >= 1:
        sum += x % 10
        x //= 10
    print(sum)

# 別解
while True:
    x = input()
    if x == '0':
        break
    y = int(x)
    sum = 0
    for i in range(len(x)):
        sum += y % 10
        y //= 10
    print(sum)
