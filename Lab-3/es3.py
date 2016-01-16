class PolishNode(object):
    def __init__(self, tag, children = None):
        self.tag = tag
        self.children = children

    def eval(self):
        if self.children is None:
            return self.tag
        return PolishCalculator.operands[self.tag]([x.eval() for x in self.children])

    def __str__(self):
        if self.tag not in PolishCalculator.operands:
            return str(self.tag)
        else:
            if self.tag == "not":
                return ("(not {0})".format(self.children[0]))
            elif (self.tag == "-" or self.tag == "+") and len(self.children) == 1:
                return "({0} {1} 1)".format(self.children[0], self.tag)
            return "({0} {1} {2} )".format(self.children[0], self.tag, self.children[1])

class PolishCalculator(object):

    bools = {"T" : True, "F" : False}
    operands = {"+" : lambda x: x[0] + x[1] if len(x) > 1 else x[0] + 1,
    "-" : lambda x: x[0] - x[1] if len(x) > 1 else x[0] - 1,
    "*" : lambda x: x[0] * x[1],
    "/" : lambda x: x[0]/x[1],
    "**" : lambda x: x[0]**x[1],
    "and" : lambda x: x[0] and x[1],
    "or" : lambda x: x[0] or x[1],
    "not" : lambda x: not x[0]}

    def __init__(self):
        self._val = 0
        self._top = None

    def __str__ (self):
        return ("{0} = {1}".format(self._top, self._val))

    def __parse__(self, string):
        expr = string.split()
        stack = []
        evaluated_expr = [PolishCalculator.bools[x] if x in PolishCalculator.bools else x if x in PolishCalculator.operands else float(x) for x in expr]
        for e in evaluated_expr:
            if e not in PolishCalculator.operands:
                newnode = PolishNode(e)
            else:
                if ((e == "+" or e == "-") and len(stack) == 1) or e == "not":
                    newnode = PolishNode(e, [stack.pop()])
                else:
                    y,x = stack.pop(), stack.pop()
                    newnode = PolishNode(e, [x,y])
            stack.append(newnode)
        self._top = stack.pop()
        print (self._top)

    def eval(self, string):
        self.__parse__(string)
        self._val = self._top.eval()

if __name__ == '__main__':

    testset = ["3 3 +", "T not", "3 -", "2 3 **", "T F not and", "3 - - 2 *", "2"]
    cal = PolishCalculator()
    for t in testset:
        cal.eval(t)
        print(cal)
