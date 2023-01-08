str = input()
num = int(input())

for i in range(num):
    ord = input().split()
    ord[1] = int(ord[1])
    ord[2] = int(ord[2])
    if ord[0] == 'print':
        print(str[ord[1]:ord[2] + 1])
    elif ord[0] == 'reverse':
        # 文字列を逆順にするには一旦リストを経由する必要がある
        str = str[:ord[1]] + ''.join(list(reversed(
            str[ord[1]:ord[2] + 1]))) + str[ord[2] + 1:]
    else:
        str = str[:ord[1]] + ord[3] + str[ord[2] + 1:]
