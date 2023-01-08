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
        print(self.dct[1])


dice = Dice(list(map(int, input().split())))

dice.ord(input())
