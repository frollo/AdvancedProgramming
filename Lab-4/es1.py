import re
from functools import reduce
class MyString(str):

    def __init__(self, value):
        super(MyString, self).__init__()
        self.value = value

    def __cleanUp__(value):
        return re.sub("[\W]", "", value).lower()

    def isPalindrome(self):
        clean = MyString.__cleanUp__(self.value)
        return reduce(lambda x,y: x and y, map(lambda x: x[0]==x[1], zip(clean, clean[::-1])))

    def subtract(self, string):
        return MyString(re.sub("[" + string + "]", "", self.value))

    def __isAnagram__(self, string):
        cleanValue = sorted(list(MyString.__cleanUp__(self.value)))
        cleanString = sorted(list(MyString.__cleanUp__(self.value)))
        return reduce(lambda x,y: x and y, map(lambda x: x[0]==x[1], zip(cleanValue, cleanString)))

    def dictAnagram(self, dictionary):
        return len(list(filter(lambda x: self.__isAnagram__(x), dictionary.keys()))) > 0

if __name__ == '__main__':
    pals = ["Rise to vote, sir", "Do geese see God?", "detartrated"]
    for p in pals:
        mp = MyString(p)
        print("Is \"{0}\" palindrome? {1}".format(mp, mp.isPalindrome()))

    sub = MyString("Walter Cazzola")
    print(sub.subtract(MyString("abcwxyz")))

    diString = MyString("anagramma")
    diDict1 = {"grammana" : 1, "grandma": 3}
    diDict2 = {"chiesa": 0, "casa" : 1, "coca-cola": 2}
    print (diString.dictAnagram(diDict1))
    print (diString.dictAnagram(diDict2))
