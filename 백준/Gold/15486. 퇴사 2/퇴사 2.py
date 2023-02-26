import sys

N = int(sys.stdin.readline())

T = [0]
P = [0]
dp = [0 for _ in range(N+1)]

for i in range(N):
    t, p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    if i + T[i]-1 <= N:
        dp[i + T[i]-1] = max(dp[i + T[i] - 1], dp[i-1] + P[i])
    dp[i] = max(dp[i], dp[i - 1])
print(dp[N])

