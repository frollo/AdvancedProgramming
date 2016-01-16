class MyDict(dict):
    def __init__(self):
        super(MyDict, self).__init__()
        self._orderedKeys = []

    def __setitem__(self, key, value):
        super(MyDict, self).__setitem__(key,value)
        self._orderedKeys.append(key)
        self._orderedKeys = sorted(self._orderedKeys)

    def popitem(self):
        k = self._orderedKeys.pop()
        v = super(MyDict, self).pop(k)
        return (k,v)

    def items(self):
        return [super(MyDict, self).__getitem__(x) for x in self._orderedKeys]

    def __str__(self):
        pairs = [(x,super(MyDict, self).__getitem__(x)) for x in self._orderedKeys]
        return "{"  + " , ".join(["{0} : {1}".format(x[0],x[1]) for x in pairs]) + "}"

if __name__ == '__main__':
    d = MyDict()
    d["a"] = 1
    d["b"] = 2
    d["c"] = 3
    d["d"] = 4

    oldd = {"a" : 1, "b" : 2, "c" : 3, "d" : 4}
    print (d)
    print (oldd)
