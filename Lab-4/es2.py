class SocialNode(object):
    def __init__(self, name):
        self.name = name
        self.connections = list()

    def addConnection(self, tag, other):
        self.connections.append((tag, other))
        other.connections.append((tag, self))

    def __visit__(self, visited=None):
        if visited is None: visited = set()
        visited.add(self)
        toVisit = [x[1] for x in self.connections if x[1] not in visited]
        for friend in toVisit:
            if friend not in visited:
                visited = visited.union(friend.__visit__(visited))
        return visited

    def __str__(self):
        visited = self.__visit__()
        string = ""
        for v in visited:
            friends = ["\t{0} with {1}\n".format(x[0], x[1].name) for x in v.connections]
            string = string + v.name + ":\n" + "".join(friends)
        return string

if __name__ == '__main__':
    lollo = SocialNode("Lorenzo Rossi")
    marco = SocialNode("Marco Odore")
    luca = SocialNode("Luca Rossi")
    lollo.addConnection("works", marco)
    lollo.addConnection("friend", luca)

    print(lollo)
