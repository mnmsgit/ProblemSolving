import sys

K = int(sys.stdin.readline())

stack = []
for i in range(K):
    money = int(sys.stdin.readline())
    if not money:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))