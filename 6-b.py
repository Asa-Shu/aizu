n = int(input())

lst = []
for i in range(n):
    lst.append(input())

man = []
for i in range(1, 14):
    man.append(f'S {i}')
for i in range(1, 14):
    man.append(f'H {i}')
for i in range(1, 14):
    man.append(f'C {i}')
for i in range(1, 14):
    man.append(f'D {i}')

for i in lst:
    man.remove(i)

for i in man:
    print(i)


# 順番を考慮しないならsetでもかける
# n = int(input())

# lst = set()
# for i in range(n):
#     lst.add(input())

# man = set()
# for i in range(1, 14):
#     man.add(f'S {i}')
# for i in range(1, 14):
#     man.add(f'H {i}')
# for i in range(1, 14):
#     man.add(f'C {i}')
# for i in range(1, 14):
#     man.add(f'D {i}')

# for i in man - lst:
#     print(i)



