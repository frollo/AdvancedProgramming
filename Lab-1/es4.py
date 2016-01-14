from functools import reduce

def identity(size):
    return [[1 if x == y else 0 for x in range(0, size)] for y in range(0, size)]

def square (size):
    return [[x + (y * size ) for x in range(0, size)] for y in range(0,size)]

def transpose (matrix):
    #return [[matrix[j][i] for j in range(0, len(matrix[i]))] for i in range(0, len(matrix))]
    return [[m[i] for m in matrix] for i in range(0, len(matrix[0]))]

def multiply (a,b):
    if len(a[0]) != len(b):
        raise Exception()

    return [[sum([e*f for e,f in zip(c,d)]) for d in transpose(b)] for c in a]

if __name__ == '__main__':
    mi = identity(4)
    for row in mi:
        print ("\t".join([str(x) for x in row]))

    print("\n")
    ms = square(4)
    for row in ms:
        print ("\t".join([str(x) for x in row]))

    print("\n")
    mt = transpose([[0,1,2],[3,4,5]])
    for row in mt:
        print ("\t".join([str(x) for x in row]))

    print("\n")
    mp = multiply(mi,mi)
    for row in mp:
        print ("\t".join([str(x) for x in row]))
