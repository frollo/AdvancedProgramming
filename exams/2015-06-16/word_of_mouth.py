with open('exams/2015-06-16/dictionary.txt', "r") as f:
    admitted_words = [line.strip() for line in f]

def iterchain(start, stop, pastvalues = []):
    pastvalues.append(start)
    if start == stop:
        return [[stop]]
    l_stop = list(stop)
    l_start = list(start)
    found_paths = list()
    changes = list()
    for i in range(len(l_stop)):
        if l_stop[i] != l_start[i]:
            changes += ["".join(l_start[0:i] + [x] + l_start[i+1::]) for x in list('abcdefghijklmnopqrstuwxyz')]

    changes = [x for x in changes if (x not in pastvalues) and (x in admitted_words)]
    for next_step in changes:
        newpast = pastvalues.copy()
        for path in iterchain(next_step, stop, newpast):
            found_paths.append([start] + path)
    return found_paths


def chain(start, stop):
    result = ""
    for ch in iterchain(start, stop):
        result += str(ch) + "\n"
    return result

if __name__ == '__main__':
  print("### witness → fatness")
  print(chain("witness", "fatness"))
  print("### warning → earring")
  print(chain("warning", "earring"))
  print("### sailing → writing")
  print(chain("sailing", "writing"))
