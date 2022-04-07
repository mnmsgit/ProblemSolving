import sys

n = int(sys.stdin.readline())
for i in range(n):
    S = sys.stdin.readline().split()
    print("Case #" + str(i + 1) + ":", end=" ")
    for _ in range(len(S)):
        print(S.pop(), end=" ")
