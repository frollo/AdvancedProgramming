import calendar
if __name__ == '__main__':
    for i in range(2016,2020):
        if calendar.isleap(i):
            print(i)
            break
    print (calendar.leapdays(1999,2051))
    weekdays = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
    print (weekdays[calendar.weekday(2016, 7, 29)])
