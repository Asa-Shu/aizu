a, b, c = map(int, input().split())
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <= a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else:
    print(c, b, a)

# 別解
a, b, c = map(int, input().split())
# 5 3 2
if a > b:
    a, b = b, a  # 3 5 2
if b > c:
    b, c = c, b  # 3 2 5
if a > b:
    a, b = b, a  # 2 3 5

print(a, b, c)
