# 코드1

import sys

N = int(sys.stdin.readline())

mod = 1000000000

# dp[현재자리][0~9가 올때의 경우][방문 여부(bitmask)]
dp = [[[0]*(1<<10) for j in range(10)] for i in range(N+1)]

# 첫 자리수 초기화
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            ## 자리수가 0인 경우 직전 자리수는 1로 고정
            if j == 0:
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]
            ## 자리수가 9인 경우 직전 자리수는 8로 고정
            elif j == 9:
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]
            else:
                dp[i][j][(1 << j) | k] += dp[i - 1][j - 1][k]
                dp[i][j][(1 << j) | k] += dp[i - 1][j + 1][k]
            dp[i][j][(1 << j) | k] %= mod

ans = 0
# for i in range(1, 10):
#     # 0~9까지 모든 수가 bitmask된 경우만 더하기
#     print(dp[N-1][i][(1<<10) - 1])
#     ans += dp[N][i][(1<<10) - 1]
#     ans %= mod
for i in range(10):
    ans = (ans+dp[N][i][(1<<10)-1])%mod
print(ans)
