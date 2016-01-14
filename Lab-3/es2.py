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
