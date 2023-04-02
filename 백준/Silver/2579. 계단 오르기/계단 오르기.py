# dp 대표문제
# 매번 전단계 계단을 밟을 지 안 밟을 지에 따라 경우가 2개이므로 배열을 2차원으로 구성

import sys

N = int(sys.stdin.readline())
dp = [[0,0] for _ in range(N+1)]
stairs = [int(sys.stdin.readline()) for _ in range(N)]
stairs.insert(0,0)

dp[1][0], dp[1][1] = stairs[1],stairs[1]

for i in range(2,N+1):
    # 전 계단을 안 밟는 경우
    dp[i][0] = max(dp[i-2]) + stairs[i]
    # 전 계단을 밟는 경우
    dp[i][1] = dp[i-1][0] + stairs[i]

print(max(dp[N]))
