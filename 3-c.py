while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x < y:
        print(x, y)
    else:
        print(y, x)

# passを明示するなら以下のよう
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    elif x > y:
        x, y = y, x
    else:
        pass  # なにもしない
    print(x, y)
