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
