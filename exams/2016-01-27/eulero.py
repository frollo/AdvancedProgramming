from math import factorial

def pi_series():
    past = 0.0
    den = 1.0
    sign = 1.0
    while True:
        past += (4.0 / (den * sign))
        den = den + 2.0
        sign = sign * -1.0
        yield past

def e_series():
    den = 1
    past = 1
    yield past
    while True:
        past += 1 / factorial(den)
        den += 1
        yield past

def euler_accelerator(serie):
    s0 = next(serie)
    s1 = next(serie)
    s2 = next(serie)
    while True:
        yield s2 - (((s2 - s1)**2) / (s0 - 2*s1 + s2))
        s0, s1, s2 = s1, s2, next(serie)

def firstn(g, n):
   for i in range(n):
      yield next(g)

if __name__ == '__main__':
   print("exact value for π :- {0:.16}".format(3.14159265358979))
   print("old(π) :-", list(firstn(pi_series(), 7)))
   print("new(π) :-", list(firstn(euler_accelerator(pi_series()), 7)))
   print("exact value for ε :- {0:.16}".format(2.71828182845904))
   print("old(ε) :-", list(firstn(e_series(), 7)))
   print("new(ε) :-", list(firstn(euler_accelerator(e_series()), 7)))
