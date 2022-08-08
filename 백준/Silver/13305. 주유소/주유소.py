import sys
N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
oil = list(map(int, sys.stdin.readline().split()))
pay = 0
min_oil = oil[0]
for i in range(N-1):
    min_oil = min(min_oil, oil[i])
    pay += min_oil * road[i]

print(pay)


