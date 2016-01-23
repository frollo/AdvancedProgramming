from functools import reduce
from traceback import print_stack

def memorization(funct):
    old_data = dict()

    def dec_memorization(*args):
        if  args not in old_data:
            old_data[args] = funct(*args)
        return old_data[args]

    return dec_memorization

def logging (funct):
    def dec_logging(*args):
        log = open("log.log", "a")
        log.write("{0}({1})\n".format(funct.__name__, args))
        log.close()
        return funct(*args)
    return dec_logging

def stack_trace(function):
    def dec_stack_trace(*args):
        print_stack()
        return function(*args)
    return dec_stack_trace


class MyMath():
    @memorization
    @stack_trace
    def fib(level):
        if level <= 2:
            return [1 for i in range(level)]
        past = MyMath.fib(level-1)
        return past + [past[-1] + past[-2]]
    @memorization
    @logging
    def fact(n):
        return reduce(lambda x,y : x * y, [i for i in range(1, n+1)])

if __name__ == '__main__':
    funo = MyMath.fact(4)
    fdue = MyMath.fact(4)
    print(funo)
    print(fdue)
    MyMath.fib(2)
    MyMath.fib(3)
    MyMath.fib(4)
