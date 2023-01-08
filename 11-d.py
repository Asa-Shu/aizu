class Dice:

    def __init__(self, lst: 'list[int]'):
        self.dct = dict(zip(range(1, 7), lst))

    def ord(self, s: str):
        if s == 'E':
            dammy = self.dct[1]
            self.dct[1] = self.dct[4]
            self.dct[4] = self.dct[6]
            self.dct[6] = self.dct[3]
            self.dct[3] = dammy
        elif s == 'N':
            dammy = self.dct[1]
            self.dct[1] = self.dct[2]
            self.dct[2] = self.dct[6]
            self.dct[6] = self.dct[5]
            self.dct[5] = dammy
        elif s == 'S':
            dammy = self.dct[1]
            self.dct[1] = self.dct[5]
            self.dct[5] = self.dct[6]
            self.dct[6] = self.dct[2]
            self.dct[2] = dammy
        else:
            dammy = self.dct[1]
            self.dct[1] = self.dct[3]
            self.dct[3] = self.dct[6]
            self.dct[6] = self.dct[4]
            self.dct[4] = dammy


n = int(input())
dices = []
for i in range(n):
    dices.append(Dice(list(map(int, input().split()))))

for i in range(n):
    for j in range(i + 1, n):
        for k in ["N", "N", "N", 'E', 'E', 'S', 'S', 'W'] * 3:  # 24通りでさいころを一巡できる
            dices[j].ord(k)
            if dices[i].dct == dices[j].dct:
                print('No')
                exit()
print('Yes')
