x = input()
lst = list(map(int, input().split()))
lst.reverse()
# .sort(reverse=True) は降順
print(" ".join(map(str, lst)))  # mapオブジェクトはリストにしなくてもjoinに使える
