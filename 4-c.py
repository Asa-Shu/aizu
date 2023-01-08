while True:
    a, op, b = input().split()
    a = int(a)
    b = int(b)
    # a, b = map(int, [a, b]) でも可
    if op == "?":
        break
    elif op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    else:
        print(a // b)
