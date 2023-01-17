# import sys
# 
# C, N = map(int, sys.stdin.readline().split())
# 
# item = [[0, 0] for i in range(N+1)]
# for i in range(1, N+1):
#     cost, people = map(int, sys.stdin.readline().split())
#     item[i][0] = cost
#     item[i][1] = people
# 
# dp = [sys.maxsize for i in range(C+100)]
# dp[0] = 0
# item.sort(key=lambda x: x[0])
# 
# for cost, people in item:
#     for i in range(people, people+100):
#         dp[i] = min(dp[i-people]+cost, dp[i])
# 
# print(min(dp[C:]))
import sys

input = sys.stdin.readline
INF = 1e9

c, n = map(int, input().split())
data = []

min_cost = [INF] * (c+100)
min_cost[0] = 0

for _ in range(n):
    # cost, cus
    data.append(list(map(int, input().split())))

# cost 작은 순서로 정리
data_sort = sorted(data, key = lambda x: x[0])


for cost, cus in data_sort:
    for i in range(cus, c+100):
        min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])

print(min(min_cost[c:]))