class PascalRow(object):
    def __init__(self, previous = None):
        self.index = 0
        if previous is None:
            self.values = [0]
        else:
            self.values = [1] + [previous.values[i] + previous.values[i + 1] for i in range(len(previous.values) -1)] + [1]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.values):
            raise StopIteration
        value = self.values[self.index]
        self.index += 1
        return value

    def __prev__(self):
        self.index -= 1
        if self.index < 0:
            raise StopIteration
        return self.values[self.index]


class PascalTriangle(object):

    def __init__(self, max):
        self.previous = []
        self.max = max
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max:
            raise StopIteration
        self.count += 1
        if len(self.previous) >= self.count:
            return self.previous[self.count]
        current = PascalRow(self.previous[-1] if len(self.previous) > 0 else None)
        self.previous.append(current)
        return current

    def __prev__(self):
        self.count -= 1
        if self.index < 0:
            raise StopIteration
        return self.previous[self.count]

if __name__ == '__main__':
    p = PascalTriangle(10)
    for a in p:
        print("\t".join([str(x) for x in a]))
