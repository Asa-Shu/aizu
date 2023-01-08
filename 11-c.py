# 改良の余地あり
import random


class Dice:

    def __init__(self, lst: 'list[int]'):
        self.dct = dict(zip(range(1, 7), lst))

    def ord(self, s: str):
        for i in range(len(s)):
            if s[i] == 'E':
                dammy = self.dct[1]
                self.dct[1] = self.dct[4]
                self.dct[4] = self.dct[6]
                self.dct[6] = self.dct[3]
                self.dct[3] = dammy
            elif s[i] == 'N':
                dammy = self.dct[1]
                self.dct[1] = self.dct[2]
                self.dct[2] = self.dct[6]
                self.dct[6] = self.dct[5]
                self.dct[5] = dammy
            elif s[i] == 'S':
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

    def right(self, lst: 'list[int]'):
        while True:
            word = ''.join(random.choices('ENSW', k=3))
            self.ord(word)
            if self.dct[1] == lst[0] and self.dct[2] == lst[1]:
                print(self.dct[3])
                break

    def rolling(self, dice):
        for _ in range(100):
            word = ''.join(random.choice('ENSW'))
            self.ord(word)
            flag = 0
            if self.dct == dice.dct:
                print('Yes')
                flag = 1
                break
        if flag == 0:
            print('No')


*L1, = map(int, input().split())
*L2, = map(int, input().split())
dice1 = Dice(list(L1))
dice2 = Dice(list(L2))

dice1.rolling(dice2)

# p = (0, 0, 0, 1, 1, 2, 2, 3) * 3
# サイコロは24回回転すれば全部試せる
