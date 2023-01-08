# 展開して出力する
# " ".join(strのリスト) 使ってもいいけどstr型のリスト作るためには内包表記とか使わないといけないし得策ではないかも
r, c = map(int, input().split())
sum1 = [0 for a in range(c + 1)]
for i in range(r):
    lst = list(map(int, input().split()))
    lst.append(sum(lst))
    sum1 = list(map(lambda x, y: x + y, sum1, lst))
    print(*lst)  # *はリストを展開する
print(*sum1)
