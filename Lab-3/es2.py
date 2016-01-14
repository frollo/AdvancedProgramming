from functools import reduce

class Monoid(object):
    threshold = 100

    def testAssociativity(testset, operation):
        if len(testset) > threshold:
            testset = testset[0:threshold]
        return reduce(lambda x,y: x and y, [True if operation(operation(x,y),z) == operation(operation(x,z),y) else False\
        for x in testset for y in testset for z in testset])

    def testIdentity(testset, operation, identity):
        if len(testset) > threshold:
            testset = testset[0:threshold]
        return reduce(lambda x,y: x and y, [True if operation(x,identity) == x else False for x in testset])
