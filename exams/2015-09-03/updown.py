from re import split

class UpDownFile(object):
    def __init__(self,filename):
        self.stack = list()
        self.pointer = 0
        self.infile = open(filename, "r")

    def __iter__(self):
        self.pointer = 0
        return self
    
    def __next__(self):
        self.pointer += 1
        while self.pointer > len(self.stack):
            try:
                nextLine = next(self.infile)
            except StopIteration:
                raise StopIteration
            
            words = [w.strip() for w in split("[\s\,\.\"\'\(\)\[\]\{\}\:]", nextLine) if w.strip() != ""]
            self.stack += words
        return self.stack[self.pointer - 1]

    def ungetw(self):
        self.pointer -= 1
        return self.stack[self.pointer -1]

