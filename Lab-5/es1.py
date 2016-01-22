import re
from functools import reduce
class TicTacToe(str):

    def __init__(self, value):
        super(TicTacToe, self).__init__()
        self.value = value

    def __cleanUp__(value):
        return re.sub("[\W]", "", value).lower()

    def isPalindrome(self):
        clean = TicTacToe.__cleanUp__(self.value)
        return reduce(lambda x,y: x and y, map(lambda x: x[0]==x[1], zip(clean, clean[::-1])))

    def __compose_columns__(self,matrix):
        return ["".join([matrix[x][y] for x in range(3)]) for y in range(3)]

    def __compose_diagonal__(self,matrix):
        return ["".join([matrix[x][x] for x in range (3)]), "".join(matrix[x][x] for x in range(0,3,-1))]

    def __is_winner__(self, player):
        if self.value.count(player) < 3:
            return False
        lines = [self.value[i] if len(self.value) > i else " " for i in range(9)]
        matrix = [lines[0:3], lines[3:6], lines[6:9]]
        winning_rows = ["".join(matrix[0]), "".join(matrix[1]), "".join(matrix[2])] + self.__compose_columns__(matrix) + self.__compose_diagonal__(matrix)
        print (self.value)
        print (winning_rows)
        return reduce(lambda x,y: x or y, map(lambda x: x.count(player) == 3, winning_rows))

    def validate(self):
        x = self.value.count("X")
        o = self.value.count("O")
        empty = self.value.count(" ")
        if (x + o > 9) or (x + o + empty < len(self.value)) or (abs(x - o) > 1):
            return "Invalid"
        wx = self.__is_winner__("X")
        wo = self.__is_winner__("O")
        if (wx and wo) or (wx and o > x) or (wo and x > o):
            return "Invalid"
        return (wx and "X") or (wo and "O") or (x + o < 9 and "Moves") or "Even"
