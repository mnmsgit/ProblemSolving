# dp 심화문제
# rgb1 과 다르게 table을 1차원 배열로 쓰기에 마지막에서 문제가 있음 (N 번째에서) 따라서 2차원 배열을 이용하여 dp table 채우기
import sys

# 원형 테이블과 같은 구조

# 1번을 칠하는 3가지 경우에 대해 각각의 최소값을 구하면 하면 되지 않을까?

N = int(sys.stdin.readline())

cost = [[]for _ in range(N+1)]

for i in range(N):
    cost[i] = list(map(int, sys.stdin.readline().split()))

ans = sys.maxsize

for i in range(3):
    dp = [[sys.maxsize, sys.maxsize, sys.maxsize] for _ in range(N)]

    dp[0][i] = cost[0][i]
    for j in range(1, N):
        dp[j][0] = cost[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = cost[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = cost[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)
