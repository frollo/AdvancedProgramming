from datetime import date

def __get_day_salary__(self):
    return self.__pay_per_hour__ * 8

def __get_week_salary__(self):
    return self.day_salary * 5

def __get_month_salary__(self):
    return self.week_salary * 4

def __get_yeat_salary__(self):
    return self.month_salary * 12

def __set_day_salary__(self, day_salary):
    self.__pay_per_hour__ = float(day_salary / 8)

def __set_week_salary__(self, salary):
    self.day_salary = float(salary/5)

def __set_month_salary__(self, salary):
    self.week_salary = float(salary/4)

def __set_year_salary__(self, salary):
    self.month_salary = float(salary/12)

def __spell_init__(self, name, surname, birthday, salary):
    self.__name = name
    self.__surname = surname
    self.__birthday = birthday
    self.__pay_per_hour__ = salary

def __spell_repr__(self):
            return "{0} {1}, {2}/{3}/{4}: {5}".format(self.__name, self.__surname, self.__birthday.day, self.__birthday.month, self.__birthday.year, self.__pay_per_hour__)


class Spell(type):
    def __new__(meta, classname, supers, classdict):
        classdict["__init__"] = __spell_init__
        classdict["__repr__"] = __spell_repr__
        classdict["day_salary"] = property(__get_day_salary__, __set_day_salary__)
        classdict["week_salary"] = property(__get_week_salary__, __set_week_salary__)
        classdict["month_salary"] = property(__get_month_salary__, __set_month_salary__)
        classdict["year_salary"] = property(__get_yeat_salary__, __set_year_salary__)
        return type.__new__(meta, classname, supers, classdict)

class Person(object, metaclass = Spell):
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
