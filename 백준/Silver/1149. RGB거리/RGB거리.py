# 1149


# case = [(0,1),(0,2),(1,0),(1,2),(2,0),(2,1)]
# house_col = [-1 for i in range(N)]
# for i in range(len(case)):
#     cost = price[0][case[i][0]] + price[1][case[i][1]]
#     house_col[0] = case[i][0]
#     house_col[1] = case[i][1]
#     for j in range(2, N-1):
#         cur = 3-house_col[j-1]-house_col[j-2]
#         house_col[j] = cur
#         cost += price[j][cur]
#     cost += min(price[N-1][3-house_col[N-2]-house_col[N-3]], price[N-1][house_col[N-3]])
#     if cost < min_cost:
#         min_cost = cost
# print(min_cost)


import sys

N = int(sys.stdin.readline())
price = [[]for i in range(N)]
for i in range(N):
    r,g,b = map(int,sys.stdin.readline().split())
    price[i] = [r,g,b]

case = [(1,2),(0,2),(0,1)]

dp = [[-1,-1,-1] for _ in range(N)]
dp[0] = price[0]
for i in range(1,N):
    for j in range(3):
        dp[i][j] = price[i][j] + min(dp[i-1][case[j][0]], dp[i-1][case[j][1]])
print(min(dp[N-1]))