W, H, x, y, r = map(int, input().split())
if r <= x <= W - r and r <= y <= H - r:  # & はダメ
    print("Yes")
else:
    print("No")
