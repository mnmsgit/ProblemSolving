import sys
n, k = map(int, sys.stdin.readline().split())
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
things = [(0, 0)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    things.append((w, v))  # (무게, 가치) 형태로 저장
for i in range(1, n+1):  # 목표 dp[n][k] 채우기 things[i] 반복문 안에서 다써버리자
    dp[i] = dp[i-1].copy()
    nw = things[i][0]
    nv = things[i][1]
    for weight in range(nw, k+1):
        dp[i][weight] = max(dp[i-1][weight], things[i][1]+dp[i-1][weight-things[i][0]])

print(dp[n][k])
