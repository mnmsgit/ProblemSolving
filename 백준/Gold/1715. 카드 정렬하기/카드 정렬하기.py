"""
항상 작은 숫자 2개를 더하는 것이 전체로 봐도 가장 최적의 해인 그리디 알고리즘 문제
작은 숫자 2개를 구하기 위해 우선순위 큐(heapq를 통해 구현)를 이용함
"""
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


