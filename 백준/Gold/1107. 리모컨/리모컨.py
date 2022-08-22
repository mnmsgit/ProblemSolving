import sys
N = int(sys.stdin.readline())
remote = [i for i in range(10)]
M = int(sys.stdin.readline())
broken = []
if M:
    arr = map(int, sys.stdin.readline().split())
    for element in arr:
        broken.append(element)
remote = [i for i in range(10)]
ans = abs(N-100)
str_N = str(N)
for i in range(1000001):
    possible = True
    for j in str(i):
        if int(j) in broken:
            possible = False
            break
    if possible:
        ans = min(ans, len(str(i)) + abs(i - N))
print(ans)
