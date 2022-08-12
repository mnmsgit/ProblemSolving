import sys
from heapq import *
N = int(sys.stdin.readline())
arr = []
ans = 0
for i in range(N):
    card = int(sys.stdin.readline())
    heappush(arr, card)
if N == 1:
    print(0)
else:
    while len(arr) > 1:
        a = heappop(arr)
        b = heappop(arr)
        partial_sum = a+b
        ans += partial_sum
        heappush(arr, partial_sum)
    print(ans)
