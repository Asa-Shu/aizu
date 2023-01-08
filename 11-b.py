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


dice = Dice(list(map(int, input().split())))

n = int(input())

for i in range(n):
    dice.right(list(map(int, input().split())))
