"""
dp를 이용한 문제
1. 최댓값을 구하며 2.전체탐색을 하기에 경우가 너무 많고 3.그리디 알고리즘을 쓸 수 없는 문제이기에 dp를 생각했다.
dp[n] = dp[n-2] + wine[n]
dp[n] = dp[n-3] + wine[n-1] +wine[n]
dp[n] = d[[n-1]
위의 3가지 경우중 가장 큰 경우이다.
"""
import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
wine = [int(sys.stdin.readline())for _ in range(n)]
wine.insert(0, 0)
for i in range(1, n+1):
    if i <= 2:
        dp[i] = dp[i-1] + wine[i]
    else:
        dp[i] = max(dp[i-1], max(dp[i-3]+wine[i-1], dp[i-2]) + wine[i])

print(dp[n])
