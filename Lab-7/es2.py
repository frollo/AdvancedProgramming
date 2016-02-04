from math import sqrt, ceil
from functools import reduce

def memorization(fun):
    past_values = dict()
    past_values[2] = True
    def wrapper(n):
        if n not in past_values:
            past_values[n] = fun(n)
        return past_values[n]
    return wrapper

@memorization
def is_prime(n):
    return reduce(lambda x,y: x and y, [n % i != 0 for i in range(2,ceil(sqrt(n) + 1))])

def goldbach(n):
    probable_primes = [x for x in range(2, ceil(n/2) + 1) if is_prime(x)]
    for p in probable_primes:
        if is_prime(n-p):
            return (p, n-p)
    return (None, None)

def golbach_list(n,m):
    return {x : goldbach(x) for x in range(n,m) if x % 2 == 0}

if __name__ == '__main__':
    values = [4,6,8,10,12,14,16,18,20]
    for v in values:
        x,y = goldbach(v)
        print("{0} = {1} + {2}".format(v,x,y))
    print(golbach_list(3,21))
