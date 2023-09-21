import sys


def find_next(s):
    length = len(s)
    string = list(s)
    for i in reversed(range(length-1)):
        letter = string[i]
        for j in reversed(range(i+1,length)):
            if letter < string[j]:
                string[i], string[j] = string[j], string[i]
                return "".join(string[:i+1]) + "".join(sorted(string[i+1:]))

    return "".join(string)


T = int(sys.stdin.readline())
for _ in range(T):
    word = sys.stdin.readline().strip()
    print(find_next(word))
