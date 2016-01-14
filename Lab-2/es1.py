from functools import reduce
from fractions import gcd

# 1.1 Sum all the natural numbers below one thousand that are multiples of 3 or 5
oneone = sum(list(filter(lambda x: (x % 3 == 0 ) or (x % 5 == 0), range(0,1000))))

#Result: 233168

# 1.2 Calculate the smallest number divisible by each of the numbers 1 to 20
onetwo = reduce(lambda x,y: (x*y)/gcd(x,y), list(range(2,21)))

# 1.3 Calculate the sum of the figures of 2^1000
onethree = sum([int(i) for i in str(2**1000)])

#1.4 Calculate the first term in the Fibonacci sequence to contain 1000 digits.
fibo = [1,1]
for i in range(2, 10000):
    fibo.append(fibo[i-1] + fibo[i-2])

onefour = list(filter(lambda x: len(str(x)) == 1000, fibo))[0]

if __name__ == "__main__":
    print ("1.1:\t{0}".format(oneone))
    print ("1.2:\t{0}".format(onetwo))
    print ("1.3:\t{0}".format(onethree))
    print ("1.4:\t{0}".format(onefour))
