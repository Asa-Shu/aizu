# float('inf') は無限大を表す
f_inf = float('inf')


def minkowski(n, a, b, p):
    Dp = 0
    lst = []
    for i in range(n):
        Dp += (abs(a[i] - b[i]))**p
        lst.append(abs(a[i] - b[i]))
    D = Dp**(1 / p)
    # infも比較に使える。
    if p != f_inf:
        print(f'{D:.6f}')
    else:
        print(max(lst))


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

minkowski(n, a, b, 1)
minkowski(n, a, b, 2)
minkowski(n, a, b, 3)
minkowski(n, a, b, f_inf)

# Python では float('inf') で無限大が利用できるが、そのまま書いてしまうと、都度関数呼び出しなので低速となる。最初に変数に代入して、その変数を使うと速くなる。
# float('inf') は正の整数を足そうが、掛けようが値が変わらなくて便利だが、制約が許すなら大きな整数を使用したほうがやや高速になる。

# INF = 10 ** 18

# def minkowski(n, a, b, p):
#     Dp = 0
#     for i in range(n):
#         Dp += (abs(a[i] - b[i]))**p
#     D = Dp**(1 / p)
#     print(f'{D:.8f}')

# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))

# minkowski(n, a, b, 1)
# minkowski(n, a, b, 2)
# minkowski(n, a, b, 3)
# minkowski(n, a, b, float('inf'))
# これだと挙動おかしくなる
# input:
# 3
# 1 2 3
# 2 0 4
# output:
# 4.00000000
# 2.44948974
# 2.15443469
# 2.00000000となるべきところが1.00000000になってしまう、原因不明

# 別解
n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

minkowski = [0] * 4
# 要素数で初期化
for i in range(3):
    sum = 0
    for j in range(n):
        sum += (abs(x[j] - y[j]))**(i + 1)
    minkowski[i] = sum**(1 / (i + 1))

lst = []
for j in range(n):
    lst.append(abs(x[j] - y[j]))
minkowski[3] = max(lst)

print(*minkowski, sep='\n')
