import re
from functools import reduce
class MyString(str):

    def __init__(self, value):
        super(MyString, self).__init__()
        self.value = value

    def isPalindrome(self):
        clean = re.sub("[\W]", "", self.value)
        clean = clean.lower()
        return reduce(lambda x,y: x and y, map(lambda x: x[0]==x[1], zip(clean, clean[::-1])))

if __name__ == '__main__':
    pals = ["Rise to vote, sir", "Do geese see God?", "detartrated"]
    for p in pals:
        mp = MyString(p)
        print("Is \"{0}\" palindrome? {1}".format(mp, mp.isPalindrome()))
