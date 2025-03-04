import sys
import heapq
from collections import defaultdict
# 1. 삽입

# 2. 삭제
# 2.1 우선순위가 가장 낮은 것을 삭제

# 2.2 우선순위가 가장 낮은 높은 것 삭제


# 2개의 우선순위 큐 사용 + 일관성 관리를 위한 map 사용


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    minheap, maxheap = [], []
    hashmap = defaultdict(int)
    k = int(input())
    for i in range(k):
        sig, num = input().split()
        num = int(num)
        if sig == 'I':
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
            hashmap[num] += 1
        elif sig == 'D':
            if num == 1:
                while maxheap:
                    extract_num = heapq.heappop(maxheap)
                    extract_num = -extract_num
                    if hashmap[extract_num] > 0:
                        hashmap[extract_num] -= 1
                        break
            elif num == -1:
                while minheap:
                    extract_num = heapq.heappop(minheap)
                    if hashmap[extract_num] > 0:
                        hashmap[extract_num] -= 1
                        break
            else:
                print('ERROR')
            pass
        else:
            print("ERROR")
    while minheap and hashmap[minheap[0]] == 0:
        heapq.heappop(minheap)
    while maxheap and hashmap[-maxheap[0]] == 0:
        heapq.heappop(maxheap)
    if not minheap or not maxheap:
        print("EMPTY")
    else:
        print(-maxheap[0], minheap[0])