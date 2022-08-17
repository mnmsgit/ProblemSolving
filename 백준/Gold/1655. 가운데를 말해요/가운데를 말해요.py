import sys
import heapq
l_heap = []   # 최대힙
r_heap = []  # 최소힙
mid = 0
N = int(sys.stdin.readline())
for i in range(N):
    num = int(sys.stdin.readline())
    if not i:
        mid = num
        print(mid)
        continue
    if mid <= num:
        heapq.heappush(r_heap, num)
    else:
        heapq.heappush(l_heap, -num)
    if len(r_heap) - len(l_heap) == 2:
        r_min = heapq.heappop(r_heap)
        heapq.heappush(l_heap, -min(mid, r_min))
        mid = max(mid, r_min)
    elif len(r_heap) < len(l_heap):
        l_max = -heapq.heappop(l_heap)
        heapq.heappush(r_heap, max(mid, l_max))
        mid = min(mid, l_max)
    print(mid)

