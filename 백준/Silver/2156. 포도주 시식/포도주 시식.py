import sys
n = int(sys.stdin.readline())
dp = [0 for _ in range(n+1)]
wine = [int(sys.stdin.readline())for _ in range(n)]
wine.insert(0, 0)
for i in range(1, n+1):
    if i <= 2:
        dp[i] = dp[i-1] + wine[i]
    else:
        dp[i] = max(dp[i-3]+wine[i-1] , dp[i-2]) + wine[i]
    if dp[i-1]>= dp[i]:
        dp[i] = dp[i-1]

print(dp[n])
