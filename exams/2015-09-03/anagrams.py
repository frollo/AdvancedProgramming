
def hash(word):
    symbols = dict()
    for letter in list(word.lower()):
        if letter in symbols:
            symbols[letter] += 1
        else:
            symbols[letter] = 1

    h = ""
    for k,v in sorted(symbols.items()):
        h += "{0}--{1}".format(k,v)
    return h

def compile_dict(filename="wordlist-anagrams.txt"):
    with open(filename, "r") as f:
        words = [w.strip() for w in f]
    hashes = dict()
    for w in words:
        h = hash(w)
        if h in hashes:
            hashes[h].append(w)
        else:
            hashes[h] = [w]
    return hashes

hashes = compile_dict()

def anagrams(filename):
    hashes = compile_dict(filename)
    found_anagrams = {k : sorted(v) for k,v in hashes.items() if len(v) > 2}

    for k,v in sorted(found_anagrams.items(), key=lambda x: x[1][0]):
        print("{0}\t\t:- {1}".format(v[0], ", ".join(v[1:])))

def anagram(word):
    h = hash(word)
    print ("Anagram {0}\t\t:- {1}".format(word, ", ".join([w for w  in hashes[h] if w != word])))


if __name__ == "__main__":
    anagrams("wordlist-anagrams.txt")
    anagram("resin")
    anagram("grenade")
    anagram("exam")
    anagram("stair")
    anagram("marble")
    anagram("arrest")
