from datetime import date
from types import FunctionType

def multitrigger(func):
    func.counter = 0
    def wrapper(*args):
        func.counter += 1
        if func.counter == 2:
            func.counter = 0
            return func(*args)
    return wrapper

class MultiTriggeredMethod(type):
    def __new__(meta, classname, supers, classdict):
        for k,v in classdict.items():
            if type(v) is FunctionType and k is not "__init__":
                classdict[k] = multitrigger(v)
        return type.__new__(meta, classname, supers, classdict)

class Person(object, metaclass = MultiTriggeredMethod):
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
