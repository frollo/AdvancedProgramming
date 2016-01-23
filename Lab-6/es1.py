from datetime import date, timedelta

class Person(object):
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

class Student(Person):
    def __init__(self, name, surname, birthday, lectures):
        super(Student, self).__init__(name, surname, birthday)
        self.__lectures = {x[0]:x[1] for x in lectures}

    def __getAverage(self):
        return float(sum(self.__lectures.values())/len(self.__lectures))
    average = property(__getAverage)

class Worker(Person):
    def __init__(self, name, surname, birthday, pay_per_hour):
        super(Worker, self).__init__(name, surname, birthday)
        self.__pay_per_hour = pay_per_hour

    def __get_day_salary__(self):
        return self.__pay_per_hour * 8

    def __get_week_salary__(self):
        return self.__get_day_salary__() * 5

    def __get_month_salary__(self):
        return self.__get_week_salary__() * 4

    def __get_yeat_salary__(self):
        return self.__get_month_salary__() * 12

    def __set_day_salary__(self, day_salary):
        self.__pay_per_hour = float(day_salary / 8)

    def __set_week_salary__(self, salary):
        self.__set_day_salary__(float(salary/5))

    def __set_month_salary__(self, salary):
        self.__set_week_salary__(float(salary/4))

    def __set_year_salary__(self, salary):
        self.__set_month_salary__(float(salary/12))

    day_salary = property(__get_day_salary__, __set_day_salary__)
    week_salary = property(__get_week_salary__, __set_week_salary__)
    month_salary = property(__get_month_salary__, __set_month_salary__)
    year_salary = property(__get_yeat_salary__, __set_year_salary__)

class Wizard(Person):
    def __init__(self, name, surname, birthday):
        super(Wizard, self).__init__(name, surname, birthday)

    def __getAge__(self):
        return (date.today() - self.getBirthday()).days

    def __changeAge__(self, days):
        self.setBithday = date.today() - timedelta(days=days)

    age = property(__getAge__, __changeAge__)
