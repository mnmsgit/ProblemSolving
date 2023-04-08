"""
최소힙 구현하는 기초적 문제
heapq 라이브러리 이용
"""
import heapq
import sys

N = int(sys.stdin.readline())
hq = []
for _ in range(N):
    element = int(sys.stdin.readline())
    if not element:
        if hq:
            print(heapq.heappop(hq))
        else:
            print(0)
    else:
        heapq.heappush(hq,element)
