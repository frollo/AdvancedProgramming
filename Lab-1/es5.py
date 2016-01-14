import os
import sys
from functools import reduce
from itertools import islice

def cat(args):
    for a in args:
        fin = open(a, "r")
        for line in fin:
            print(line, end="")
        fin.close()
        print("\n")

def chmod(files, perms):
    for f in files:
        os.chmod(f, perms)

def more(infile):
    with open(infile, "r" ) as fin:
        while True:
            next_lines = list(islice(fin, 30))
            if not next_lines:
                break
            for line in next_lines:
                print(line, end="")
            input("$")
