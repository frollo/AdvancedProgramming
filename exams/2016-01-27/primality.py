from math import sqrt, log, floor
from random import sample
from functools import reduce

def trialdivision(num):
    for div in range(2,floor(sqrt(num)) + 1):
        if num % div == 0:
            return False
    return True

def lucaslehmerserie(value, module):
    if value == 0:
        return 4
    return (lucaslehmerserie(value - 1, module)**2 - 2) % module

def lucaslehmer(num):
    p = log(num + 1, 2)
    return lucaslehmerserie(p - 2, num) == 0


def littlefermat(num):
    return len([elem for elem in range(2,int(log(num))+1,3) if pow(elem, num-1, num) !=1])==0

def is_prime(num):
    return (num <= 10000 and trialdivision(num)) or ( (num > 10000 and num <= 524280) and lucaslehmer(num) ) or littlefermat(num)


if __name__ == '__main__':
    def test_primes(vl):
      if len(vl)>0:
         print("{:14d} :- {}".format(vl[0], is_prime(vl[0])))
         test_primes(vl[1:])


    test_primes([25, 127, 8191, 131071, 524286, 524287, 524288, 2147483647])
