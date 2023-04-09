"""
기초적인 배낭문제(한정된 자원속에서 최선의 결과를 얻어내는 문제)
dp를 이용한 이유: 최댓값을 구할 때 그리디가 적용되지 못하며 브루트포스는 시간복잡도가 매우 큼o(2**n)
dp의 행은 물품 열은 최대무게를 의미한다.
(무게 = w,가치 = v)인 물건을 넣기 위해서는 1. w~ k까자 넣을 수 있으며 2. n = i-1에서 무게가 w만큼 남아 있어햐 한다.
"""
import sys
n, k = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
things = [(0, 0)]
for i in range(1, n+1):  # 목표 dp[n][k] 채우기 things[i] 반복문 안에서 다써버리자
    w, v = map(int, sys.stdin.readline().split())
    dp[i] = dp[i-1].copy()
    for weight in range(w, k+1):
        dp[i][weight] = max(dp[i-1][weight], v + dp[i-1][weight-w])

print(dp[n][k])
