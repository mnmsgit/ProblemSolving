"""
플로이드-워셜 알고리즘을 그대로 구현해볼 수 있는 문제
dp를 이용하며 3중 for 문이 필요한 문제
"""
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

cost = [[sys.maxsize for _ in range(n+1)]for _ in range(n+1)]

dp = [[sys.maxsize for _ in range(n+1)]for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    cost[a][b] = min(cost[a][b],c)

for k in range(1, n+1):
    for first in range(1, n+1):
        for des in range(1, n+1):
            if first != des:
                cost[first][des] = min(cost[first][des], cost[first][k]+cost[k][des])

for i in range(1,n+1):
    for j in range(1,n+1):
        if cost[i][j] == sys.maxsize:
            print(0, end=" ")
        else:
            print(cost[i][j], end=" ")
    print()