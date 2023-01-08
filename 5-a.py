while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):  # 行に関しての処理
        for j in range(W):  # 列に関しての処理
            print("#", end="")  # end="" は出力時に改行したくない場合に使う
        print()  # 改行
    print()  # 改行
