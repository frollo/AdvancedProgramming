from datetime import date

def dCounter(fun, classname):
    def dCounterf(*args):
        Counter.counters[classname] += 1
        return fun(*args)
    return dCounterf

class Counter(type):
    counters = dict()
    def __new__(meta, classname, supers, classdict):
        if classname not in Counter.counters:
            Counter.counters[classname] = 0
        classdict["__init__"] = dCounter(classdict["__init__"], classname)
        return type.__new__(meta, classname, supers, classdict)

class Person(object, metaclass = Counter):
    def __init__(self, name, surname, birthday):
        self.__name = name
        self.__surname = surname
        self.__birthday = birthday

    def getName(self):
        return self.__name

    def setName(self, newname):
        self.__name = newname

    def getSurname(self):
        return self.__surname

    def setSurname(self, surname):
        self.__surname = surname

    def getBirthday(self):
        return self.__birthday

    def setBithday(self, birthday):
        self.__birthday = birthday

    def __repr__(self):
        return "{0} {1}, {2}/{3}/{4}".format(self.__name, self.__surname, self.__birthday.day, self.__birthday.month, self.__birthday.year)


if __name__ == '__main__':
    PUno = Person("Lorenzo", "Rossi", date(1991,5,28))
    print(Counter.counters)
    PDue = Person("Lorenzo", "Rossi", date(1991,5,28))
    print(Counter.counters)
