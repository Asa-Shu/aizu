# 文字列は辞書順比較できる
num = int(input())
taro = 0
hanako = 0
for i in range(num):
    x, y = input().split()
    if x == y:
        hanako += 1
        taro += 1
    elif x < y:
        hanako += 3
    else:
        taro += 3

print(taro, hanako)
