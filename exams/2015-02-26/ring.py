import unittest
from functools import reduce

### TEST ###
def add_test(ring, name):
    class testRing(unittest.TestCase):
        def test_closure(self):
            print("Testing closure on {}".format(name))
            closures = reduce(lambda x,y: x and y, [(x + y).inSet() and (x * y).inSet() for x in ring.signature() for y in ring.signature()])
            self.assertTrue(closures, msg="### {} does not respect closure property ###".format(name))
        def test_commutativity(self):
            print("Testing commutativity on {}".format(name))
            comms = reduce(lambda x,y : x and y, [(x * y == y * x) for x in ring.signature() for y in ring.signature()])
            self.assertTrue(comms, msg="### {} does not respect commutativity ###".format(name))
        def test_identity_add(self):
            print("Testing sum identity on {}".format(name))
            add_ids = reduce(lambda x,y : x and y, [(x + ring.i == x) for x in ring.signature()])
            self.assertTrue(add_ids, msg="### {} does not respect addition identity ###".format(name))
        def test_identity_mul(self):
            print("Testing multiplication identity on {}".format(name))
            sum_ids = reduce(lambda x,y: x and y, [(x * ring.z == x) for x in ring.signature()])
            self.assertTrue(sum_ids, msg="### {} does not respect multiplication identity ###".format(name))
        def test_invertibility(self):
            print("Testing invertibility on {}".format(name))
            inv_checks = reduce(lambda x,y: x and y, [any( (x + y ==ring.i) for y in ring.signature()) for x in ring.signature()])
            self.assertTrue(inv_checks, msg="### {} does not respect invertibility ###".format(name))
        def test_associativity_add(self):
            print("Testing addition associativity on {}".format(name))
            assoc_add = reduce(lambda x,y: x and y, [x + (y + z) == (x + y) + z for x in ring.signature() for y in ring.signature() for z in ring.signature()])
            self.assertTrue(assoc_add, msg="### {} does not respect addition associativity ###".format(name))
        def test_associativity_mul(self):
            print("Testing multiplication associativity on {}".format(name))
            assoc_mul= reduce(lambda x,y: x and y, [x * (y * z) == (x * y) * z for x in ring.signature() for y in ring.signature() for z in ring.signature()])
            self.assertTrue(assoc_mul, msg="### {} does not respect multiplication associativity ###".format(name))
        def test_left_distributivity(self):
            print("Testing left distributivity on {}".format(name))
            left_tests = reduce(lambda x,y: x and y, [ (x * (y + z)) == ((x * y) + (x * z)) for x in ring.signature() for y in ring.signature() for z in ring.signature()])
            self.assertTrue(left_tests, msg="### {} does not respect left distributivity ###".format(name))
        def test_right_distributivity(self):
            print("Testing right distributivity on {}".format(name))
            right_tests = reduce(lambda x,y: x and y, [(y + z) * x == (y * x) + (z * x) for x in ring.signature() for y in ring.signature() for z in ring.signature()])
            self.assertTrue(right_tests, msg="### {} does not respect right distributivity ###".format(name))
    return testRing

### FUNCTIONS ###

def ringify(S,i,z,op1,op2):
    S.i = i
    S.z = z
    S.__add__ = op1
    S.__mul__ = op2
    return S

def genZ():
    yield 0
    value = 1
    while True:
        yield value
        yield -value
        value += 1

### CLASSES ###
class Z:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return str(self.value)
    def signature(n=50):
        return [Z(i) for i in range(-n, n+1)]
    def inSet(self):
        return self.value in genZ()

class nZ:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return str(self.value)
    def signature(n=50):
        return [Z(i) for i in range(-n, n+1)]
    def inSet(self):
        return self.value in genZ()

class N4:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return str(self.value)
    def signature():
        return [N4(i) for i in [0,1,2,3]]
    def inSet(self):
        return self.value in [0,1,2,3]

class B:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return str(self.value)
    def signature():
        return [B(True), B(False)]
    def inSet(self):
        return self.value in [True, False]

### TEST CASE DEFINITION ###
ring_z = ringify(Z, Z(0), Z(1), lambda x,y: Z(x.value + y.value), lambda x,y : Z(x.value * y.value))
test_z = add_test(ring_z, "(Z,+,*)")

nonring_z = ringify(nZ, nZ(1), nZ(0), lambda x,y : nZ(x.value * y.value), lambda x,y: nZ(x.value + y.value))
test_nonring_z = add_test(nonring_z, "(Z,*,+)")

ring_n4 = ringify(N4, N4(0), N4(1), lambda x,y: N4((x.value + y.value) % 4), lambda x,y: N4((x.value * y.value) % 4))
test_n4 = add_test(ring_n4, "(\{0,1,2,3\},+,*)")

nonring_b = ringify(B, B(False), B(True), lambda x,y: B(x.value | y.value), lambda x,y: B(x.value & y.value))
test_b = add_test(nonring_b, "(\{True,False\},|,&)")

all_tests = [test_z, test_nonring_z, test_n4, test_b]
suite = unittest.TestSuite()

if __name__ == '__main__':
    for tc in all_tests:
        suite.addTests(unittest.TestLoader().loadTestsFromTestCase(tc))
    unittest.TextTestRunner(verbosity=2).run(suite)
