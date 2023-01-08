i = 1
while True:
    x = int(input())
    if x == 0:
        break
    print(f"Case {i}: {x}")
    i += 1

# 別解 上記の解で、int型にキャストする必要はない
i = 1
while True:
    x = input()
    if x == '0':
        break
    print(f"Case {i}: {x}")
    i += 1

# 別解 辞書型 非効率
dct = dict()  # dctを辞書型で宣言
i = 1
while True:
    x = input()
    if x == '0':
        break
    dct[i] = x
    i += 1
for i in range(len(dct)):
    print(f'Case {i+1}: {dct[i+1]}')
