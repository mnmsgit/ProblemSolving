import sys

N = int(sys.stdin.readline())

item = [0] * N

for i in range(N):
    x = int(sys.stdin.readline())
    item[i] = x

item.sort(reverse=True)


ans =0

for i in range(N):
    if i % 3!=2:
        ans += item[i]

print(ans)