import math

# intで渡しても結局計算過程でfloatにしてくれる 出力はデフォルトで小数点以下第二位まで
a, b, C = map(float, input().split())
# 三角関数の引数は度でなく、ラジアン
C = math.radians(C)

S = a * b * math.sin(C) / 2

mukai = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(C))
L = a + b + mukai

h = b * math.sin(C)

print(S, L, h)
# 出力改行しなければいけないのに何故かこれで正解した


# 別解
a, b, C = map(int, input().split())
C = math.radians(C)

S = a * b * math.sin(C) / 2

c = math.sqrt(a ** 2 + b ** 2 - 2 * a * b * math.cos(C))
L = a + b + c

h = S * 2 / a

print(f"{S:.4f}\n{L:.4f}\n{h:.4f}")
# print(f"{S:.4f} {L:.4f} {h:.4f}")やprint(S, L, h)でも通った
