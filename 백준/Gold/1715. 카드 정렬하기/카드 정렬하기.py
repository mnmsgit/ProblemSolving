import sys
from heapq import *
N = int(sys.stdin.readline())
arr = []
ans = 0
part_sum = []
for i in range(N):
    card = int(sys.stdin.readline())
    arr.append(card)
    ans += card
heapify(arr)
while len(arr) > 2:
    a = heappop(arr)
    b = heappop(arr)
    part_sum.append(a+b)
    heappush(arr, a+b)
ans += sum(part_sum)
if N == 1:
    ans = 0
print(ans)


