import sys
stack = []


def push(n):
    stack.append(n)
    return


def top():
    return stack[-1]


def size():
    return len(stack)


def empty():
    if len(stack):
        return 0
    else:
        return 1


N = int(sys.stdin.readline().strip())

for _ in range(N):
    words = sys.stdin.readline().split()
    code = words[0]
    if code == "push":
        push(int(words[1]))
    if code == "pop":
        if not empty():
            print(stack.pop())
        else:
            print(-1)
    if code == "top":
        if not empty():
            print(top())
        else:
            print(-1)
    if code == "empty":
        print(empty())
    if code == "size":
        print(size())
