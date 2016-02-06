def memoization(fun):
    past_values = dict()
    def wrapper (*args):
        if args in past_values:
            print ("### cached value for {0} --> {1}".format(args, past_values[args]))
        else:
            past_values[args] = fun(*args)
        return past_values[args]
    return wrapper

@memoization
def fibo(n):
    if n < 3:
        return 1
    return fibo(n - 1) + fibo(n-2)

@memoization
def fact(n):
    if n < 2:
        return 1
    return n * fact(n-1)

@memoization
def sum(n,m):
    if n == 0:
        return m
    return sum(n - 1, m + 1)


if __name__ == '__main__':
    print("fibo({0}) --> {1}".format(25, fibo(25)))
    for x in range(1,25):
        print("fact({0}) --> {1}".format(x, fact(x)))
    print("sum({0}, {1}) --> {2}".format(5, 9, sum(5,9)))
    print("sum({0}, {1}) --> {2}".format(4, 10, sum(4,10)))
    print("sum({0}, {1}) --> {2}".format(13,1, sum(13,1)))
