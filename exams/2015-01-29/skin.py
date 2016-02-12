class Skin(type):
    def __new__(meta, classname, supers, classdict):
        def become(self,add_methods = {}, rem_methods = {}):
            for method in add_methods:
                self.__dict__[method.__name__] = method.__get__(self, classname)
            for method in rem_methods:
                if method in self.__dict__: del self.__dict__[method.__name__]
        classdict["become"] = become
        return type.__new__(meta, classname, supers, classdict)

if __name__ == '__main__':
    class stack(object, metaclass=Skin):
        def __init__(self, dim=10):
            self.dimension = dim
            self.top = 0
            self.data = []
        def is_empty(self): return self.top == 0
        def is_full(self): return self.top == (self.dimension-1)
        def __str__(self):
            return "Stack top :- {0} Stack dim :- {1} Stack data :- {2}".format(self.top, self.dimension, self.data)

    def push(self,arg):
        self.data.append(arg)
        self.top += 1

    def pop(self):
        self.top -= 1
        top = self.data[self.top]
        self.data = self.data[0:self.top]
        return top

    s = stack(5) # 5 is the stack dimension
    print(s)
    trend = True
    for i in range(-1,14):
        if s.is_empty():
            s.become({push}, {pop})
            trend = True
        elif s.is_full():
            s.become({pop}, {push})
            trend = False
        s.push(i) if trend else s.pop()
        print(s)
