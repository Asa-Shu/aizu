while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:  # H か W のどちらかが0なら図形にならないから片方は書かなくても良い
        break
    print("#" * W)
    for i in range(H - 2):
        print("#" + "." * (W - 2) + "#")
    print("#" * W)
    print()

# 別解  * を使わない場合
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break

    for j in range(W):
        print("#", end="")
    print()

    for i in range(H-2):  # ..#
        print('#', end='')  # 行に関しての処理
        for j in range(W-2):  # 列に関しての処理
            print(".", end="")  # end="" は出力時に改行したくない場合に使う
        print('#')  # 改行

    for j in range(W):
        print("#", end="")
    print()

    print()


# 別解

while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        if i == 0 or i == H-1:
            for j in range(W):
                print("#", end="")
            print()
        else:
            print('#', end='')
            for j in range(W-2):
                print('.', end='')
            print('#')
    print()
