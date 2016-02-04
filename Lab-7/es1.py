import sys
from re import sub

def isMinor(word):
    return (word == "the") or (word == "and") or (len(word) <= 2)

if __name__ == '__main__':
    kwicindex = list()
    counter = 0
    titles = dict()
    with open(sys.argv[1], "r") as file:
        for line in file:
            counter += 1
            line = sub("[^a-zA-Z0-9\s]", " ", line)
            line = sub("\s+", " ", line.strip())
            kwicindex += [(x, counter) for x in line.lower().split() if not isMinor(x)]
            titles[counter] = line

    for (kwic, c ) in sorted(kwicindex, key = lambda x: x[0]):
        title = titles[c]
        position = title.lower().find(kwic)
        print("{0:>5d}\t{1:>33s}{2:<40s}.".format(c, title[0:position if position < 33 else 33], title[position:40 + position:]))
