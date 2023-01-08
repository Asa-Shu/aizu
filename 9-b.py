while True:
    str = input()
    if str == '-':
        break
    # 何回シャッフルするか
    num = int(input())
    for i in range(num):
        a = int(input())
        # str = str[a:len(str)] + str[0:a]
        str = str[a:] + str[:a]
    print(str)

