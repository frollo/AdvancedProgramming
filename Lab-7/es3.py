from functools import reduce

class Matrix(object):
    def __init__(self,height, width, values):
        self.height = height
        self.width = width
        index = 0
        self.matrix = list()
        line = list()
        while index < len(values):
            line.append(values[index])
            index += 1
            if index % self.width == 0:
                self.matrix.append(line)
                line = list()

    def __eq__(self, other):
        if self.height == other.height and self.width == other.width:
            return reduce(lambda x,y: x and y, [x[0] == x[1] for x in zip(self.matrix, other.matrix)])
        else:
            return False

    def __add__(self, other):
        if self.height != other.height or self.width != other.width:
            raise Exception("Cannot sum matrix of different dimensions!")
        v1 = reduce(lambda x,y: x+y, self.matrix)
        v2 = reduce(lambda x,y: x+y, other.matrix)
        return Matrix(self.height, self.width, list(map(lambda x: x[0] + x[1], zip(v1,v2))))

    def __mul__(self, other):
        try:
            if self.height == other.width:
                mult_values = [sum([self.matrix[j][x] * other.matrix[x][i] for x in range(self.width)]) for j in range (self.width) for i in range (self.height)]
        except Exception as e:
            print(other)
            mult_values = list(map(lambda x: x * other, reduce(lambda x,y: x+y, self.matrix)))
        return Matrix(self.height, self.width, mult_values)

    def tras(self):
        new_values = [self.matrix[j][i] for i in range(self.width) for j in range(self.height)]
        return Matrix(self.height, self.width, new_values)

    def copy(self):
        return Matrix(self.height, self.width, reduce(lambda x,y: x + y, self.matrix))

    def __repr__(self):
        rep = ""
        for line in self.matrix:
            rep += "|"
            for el in line:
                rep += " {0}".format(el)
            rep += " |\n"
        return rep


if __name__ == '__main__':
    muno = Matrix(2,2,[1,2,3,4])
    mdue = Matrix(2,2,[1,2,3,4])
    mtre = Matrix(2,2,[5,6,7,8])
    mquattro = Matrix(1,1, [0])
    print(muno == mdue)
    print(mtre == mdue)
    print(mtre == mquattro)
    mcinque = muno.copy()
    print(mcinque == muno)
    print (muno + mdue)
    print (mquattro * mquattro)
    print(muno * mdue)
    mid = Matrix(2,2,[1,0,0,1])
    print(mid * muno)
