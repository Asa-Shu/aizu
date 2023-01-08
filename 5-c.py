while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            # if (j + i) % 2 == 0:
            #     print("#", end="")
            # else:
            #     print(".", end="")
            if (i + j) % 2:  # 1: True = 奇数, 0: False = 偶数
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()
