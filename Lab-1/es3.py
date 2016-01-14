def CtoC(c): return c

def CtoF(c): return (float(c) * 9.0 / 5.0) + 32.0

def CtoK(c): return float(c) + 273.15

def CtoRa(c): return CtoK(c) * (9.0/5.0)

def CtoD(c): return (100.0 - float(c)) * (3.0/2.0)

def CtoN(c): return float(c) * (33.0/100.0)

def CtoRe(c): return float(c) * (4.0/5.0)

def CtoRo(c): return (float(c) * 21.0 / 40.0) + 7.5

def FtoC(f): return (float(f) - 32.0) * (5.0/9.0)

def KtoC(k): return float(k) - 273.15

def RatoC(ra): return KtoC(ra) * (5.0/9.0)

def DtoC(d): return (100.0 - float(d)) * (2.0/3.0)

def NtoC(n): return float(n) * 100.0 / 30.0

def RetoC(re): return float(re) * 5.0 / 4.0

def RotoC (ro): return (float(ro) - 7.5) * 40.0 / 20.0

def table(value):
    rows = [[CtoC, CtoF, CtoK, CtoRa, CtoD, CtoN, CtoRe, CtoRo],
    [FtoC, CtoC, CtoK, CtoRa,CtoD, CtoN, CtoRe, CtoRo],
    [KtoC, CtoF, CtoC, CtoRa, CtoD, CtoN, CtoRe, CtoRo],
    [RatoC, CtoF, CtoK, CtoC, CtoD, CtoN, CtoRe, CtoRo],
    [DtoC, CtoF, CtoK, CtoRa, CtoC, CtoN, CtoRe, CtoRo],
    [NtoC, CtoF, CtoK, CtoRa, CtoD, CtoC, CtoRe, CtoRo],
    [RetoC, CtoF, CtoK, CtoRa, CtoD, CtoN, CtoC, CtoRo],
    [RotoC, CtoF, CtoK, CtoRa, CtoD, CtoN, CtoRe, CtoC]
    ]

    print ("C\t\tF\t\tK\t\tRa\t\tD\t\tN\t\tRe\t\tRo")
    for r in rows:
        c = r[0](value)
        row = ["{:6.2f}".format(c)] + ["{:6.2f}".format(x(c)) for x in r[1:]]
        print("\t\t".join(row))

if __name__ == '__main__':
    table(0)
    print("\n")
    table(100)
