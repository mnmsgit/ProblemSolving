import heapq
import sys

N = int(sys.stdin.readline())
hq =[]
for _ in range(N):
    element = int(sys.stdin.readline())
    if not element:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq,element)
