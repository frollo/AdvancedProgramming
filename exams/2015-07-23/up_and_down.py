class UpDownFile:
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        self.file = open(self.filename, "r")
        self.cache = []
        self.index = 0
        return self

    def __next__(self):
        if len(self.cache) > self.index:
            self.index += 1
            return self.cache[self.index - 1]

        self.index += 1
        self.cache += [self.nextW()]
        return self.cache[-1]

    def ungetw(self):
        self.index -= 1

    def nextW(self, w = ""):
        ch = self.file.read(1)
        if ch == "" :
            raise StopIteration
        if not ch in " \"\n\t.,;:?![]{}()":
            return self.nextW(w + ch)
        if w == "":
            return self.nextW()
        return w

if __name__ == '__main__':
  fiter = UpDownFile('wikipedia-excerpt.txt')
  iter(fiter)
  print('### Let\'s go up and down for a while')
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  fiter.ungetw()
  fiter.ungetw()
  fiter.ungetw()
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  print('### Let\'s finish the iteration')
  try:
    while True:
      print(next(fiter))
  except StopIteration: pass
  print('### Let\'s restart the iteration')
  iter(fiter)
  print(next(fiter))
  print(next(fiter))
  print(next(fiter))
  fiter.ungetw()
  print(next(fiter))
