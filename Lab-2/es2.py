"""
Let's write a module (a pool of functions) that given a quite large text (over than
2000 words) counts how frequent each word occurs in the text.

The text is read from a file and it is a real text with punctuation
(i.e., commas, semicolons, ...) that should be counted.

Note that words that differ only for the case should be considered the same.
"""


from collections import Counter
from functools import reduce
import re

def clean(word):
    if word[-1].isalpha():
        return [word]
    else:
        return clean(word[:-1]) + [word[-1]]

def word_count (text):
    return dict(Counter(reduce(lambda x,y : x + y, [clean(l.lower()) for l in text])))

def read_text (f):
    r = open(f, "r")
    count = dict()
    for line in r:
        words = re.findall(r"[\w\,\.;:-\?\!]+", line)
        if words == []:
            continue
        wc = word_count(words)
        for k,v in wc.items():
            if k in count:
                count[k] += v
            else:
                count[k] = v
    r.close()
    return count

if __name__ == "__main__":
    wc = read_text("lorem_ipsum.txt")
    words = 0

    for k,v in wc.items():
        words += v

    print(str(words))
