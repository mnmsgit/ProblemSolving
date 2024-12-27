"""
Greedy 기본문제

local optima가 global optima인가?
local optima: 하나의 그룹에서 최대한 많은 세일을 받는 것
global optima: 전체적으로 많은 세일을 받는 것

반례없음 -> Greedy 결정


"""
import sys

N = int(sys.stdin.readline())

item = [0] * N

for i in range(N):
    x = int(sys.stdin.readline())
    item[i] = x

item.sort(reverse=True)


ans = 0

for i in range(N):
    if i % 3 != 2:
        ans += item[i]

print(ans)