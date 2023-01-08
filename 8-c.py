import sys

# 今回は複数行にまたがるからsys.stdin.read()を使ってみた。
s = [x.lower() for x in sys.stdin.read().split()]  # input()は1行のときしか使えない
s = ''.join(s)
for i in range(26):
    print(f'{chr(97+i)} : {s.count(chr(97+i))}')
