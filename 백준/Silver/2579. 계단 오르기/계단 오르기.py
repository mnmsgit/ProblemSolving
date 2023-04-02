import sys

N = int(sys.stdin.readline())
dp = [[0,0] for _ in range(N+1)]
stairs = [int(sys.stdin.readline()) for _ in range(N)]
stairs.insert(0,0)

dp[1][0], dp[1][1] = stairs[1],stairs[1]

for i in range(2,N+1):
    dp[i][0] = max(dp[i-2]) + stairs[i]
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[N]))
