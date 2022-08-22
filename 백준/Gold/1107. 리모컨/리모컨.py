"""
전체 탐색을 이용, 근거는 : N (0 ≤ N ≤ 500,000) 이기 때문에 0-~1,000,000까지의 경우를 조사하는 것이 전체 경우이기 때문
문제 조건에서 시간제한과 범위를 잘 봐서 헛수고를 덜어야 한다는 교훈을 준 문제
"""
import sys
N = int(sys.stdin.readline())
remote = [i for i in range(10)]
M = int(sys.stdin.readline())
broken = []
if M:
    arr = map(int, sys.stdin.readline().split())
    for element in arr:
        broken.append(element)
remote = [i for i in range(10)]
ans = abs(N-100)
str_N = str(N)
for i in range(1000001):
    possible = True
    for j in str(i):
        if int(j) in broken:
            possible = False
            break
    if possible:
        ans = min(ans, len(str(i)) + abs(i - N))
print(ans)
