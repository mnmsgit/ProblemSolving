import sys

INF = int(10e5)

N, M = map(int, sys.stdin.readline().split())

dp = [INF for _ in range(M+1)]
m_i = list(map(int, sys.stdin.readline().split()))
c_i = list(map(int, sys.stdin.readline().split()))
dp[0] = 0
for i in range(1, N+1):
    item_cost = c_i[i-1]
    item_memory = m_i[i-1]
    for m in reversed(range(1, M+1)):
        if m >= item_memory:
            dp[m] = min(dp[m], dp[m-item_memory] + item_cost)
        else:
            dp[m] = min(dp[m], item_cost)
print(dp[M])
