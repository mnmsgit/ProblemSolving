"""
가운데 수를 기준으로 왼쪽과 오른쪽을 각각 최대힙 최소힙으로 구현해 heappop()했을 때 왼쪽의 배열에서 최댓값이 오른쪽 배열에서 최솟값이 나오도록 구현
새로 받은수가 기존 가운데 수보다 크면 오른쪽 배열에 작으면 왼쪽배열에 heappush한다.
이때 배열을 조정 해야 하는 경우는 
1.오른쪽 배열이 왼쪽배열에 비해 길이가 2만큼 커지거나 
2.왼쪽배열이 오른쪽배열보다 커지는 경우
2가지 이므로 해당 경우에 기존 mid와 pop한 값을 비교해 해결
"""
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

