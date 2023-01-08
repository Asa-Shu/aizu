import sys

W = input()
T = [x.lower() for x in sys.stdin.read().split()]
print(T.count(W))

# 別解
W = input()
count = 0
while True:
    str = input().split()
    if str == ['END_OF_TEXT']:
        break
    for i in range(len(str)):
        if str[i].lower() == W:
            count += 1
print(count)

# 別解
W = input()
count = 0
while True:
    str = input().split()
    if str == ['END_OF_TEXT']:
        break
    x = [i.lower() for i in str]
    count += x.count(W)
print(count)
