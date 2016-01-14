from math import sin

def factorialIt(x, count):
    while True:
        yield x
        count += 2
        x = x * (count - 1) * count

class Series (object):
    def __init__(self, x, approx):
        self.fact = factorialIt(1,1)
        self.x = x
        self.sign = -1
        self.exp = -1.0
        self.max = approx*2

    def __iter__(self):
        return self

    def __next__(self):
        if self.exp < self.max:
            self.sign = self.sign * (-1)
            self.exp = self.exp + 2.0
            return (pow(self.x, self.exp) / next(self.fact)) * self.sign
        else:
            raise StopIteration()

def taylor_sin(x, approx):
    return sum([t for t in Series(x, approx)])
