n = input()
lst = list(map(int, input().split()))
# map後にリストで渡したいときは最後にlist()にすればいい
print(min(lst), max(lst), sum(lst))
