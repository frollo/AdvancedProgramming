from functools import reduce

class Monoid(object):
    threshold = 100

    def testAssociativity(testset, operation):
        if len(testset) > Monoid.threshold:
            testset = testset[0:Monoid.threshold]
        return reduce(lambda x,y: x and y, [True if operation(operation(x,y),z) == operation(operation(x,z),y) else False\
        for x in testset for y in testset for z in testset])

    def testIdentity(testset, operation, identity):
        if len(testset) > Monoid.threshold:
            testset = testset[0:Monoid.threshold]
        return reduce(lambda x,y: x and y, [True if operation(x,identity) == x else False for x in testset])

class Group(Monoid):
    def testInversion(testset, operation, identity):
        if len(testset) > Monoid.threshold:
            reducedtestset = testset[0:Monoid.threshold]
        else:
            reducedtestset = testset

        for x in reducedtestset:
            found = False
            for y testset:
                if operation(x,y) == identity:
                    found = True
                    break
            if not found:
                return False
        return True


if __name__ == '__main__':
    #Test set 1: {True,False}, OR, False
    booleans = [True, False]
    operation = lambda x,y : x or y
    identity = False
    if Monoid.testAssociativity(booleans, operation):
        print ("OR is associative on boolean values!")
    else:
        print ("Something went wrong")

    if Monoid.testIdentity(booleans, operation, identity):
        print ("<{True,False}, OR, False> is a monoid!")
    else:
        print("Something went wrong")

    #Test set 2: Zn, (a+b)%n, 0
    def Z(n): return ([i for i in range(0,n)], lambda x,y: (x + y) % n)
    for i in range(2,40):
        myset, add = Z(i)
        if Monoid.testAssociativity(myset, add):
            print ("OK")
        else:
            print ("KO")

        if Monoid.testIdentity(myset, add, 0):
            print ("OK")
        else:
            print("KO")
