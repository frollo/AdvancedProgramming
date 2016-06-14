admitted_words = []
with open("wordlist-7.txt", "r") as f:
    for line in f:
        admitted_words += [line.strip()]

def paths(startw, endw):
    to_walk = [[startw]]

    def next_step(word, path):
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        steps = list(filter(lambda x: (x in admitted_words) and (not (x in path)), [word[0:i-1] + l + word[i::] for i in range(len(word)) for l in alphabet]))
        return (len(steps) > 1 and (steps[0], steps[1:]) ) or (len(steps) == 1 and (steps[0], [])) or (None, None)

        # if len(steps) > 1:
        #     return (steps[0], steps[1:])
        # if len(steps) == 1:
        #     return (steps[0], [])
        # return (None, None)

    for path in to_walk:
        while path[-1] != endw:
            cur_step, branches = next_step(path[-1], path)

            if not cur_step:
                path = []
                break

            to_walk += [path + [b] for b in branches]
            path += [cur_step]
        if path != []:
            yield path


def chain(startw, endw):
    return "\n".join(sorted([" ".join(i) for i in paths(startw,endw)]))

if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print("### warning → earring")
  print(chain("warning", "earring"))
  print("### sailing → writing")
  print(chain("sailing", "writing"))
