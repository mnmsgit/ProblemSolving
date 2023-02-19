import sys
import itertools

N, M = map(int,sys.stdin.readline().split())

house = []
chicken = []
city = [[] for _ in range(N)]
for i in range(N):
    city[i] = list(map(int,sys.stdin.readline().split()))
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i+1, j+1))
        if city[i][j] == 2:
            chicken.append((i+1, j+1))
chicken_distance = [[]for _ in range(len(chicken))]
for i in range(len(chicken)):
    for j in range(len(house)):
        distance = abs(chicken[i][0] - house[j][0]) + abs(chicken[i][1] - house[j][1])
        chicken_distance[i].append(distance)
# 0~ 치킨집 수-1
#  M개 뽑아야
combi = itertools.combinations(chicken_distance, M)
ans = sys.maxsize
A = list(combi)
for i in range(len(A)):
    dis = [sys.maxsize for _ in range(len(house))]
    for j in range(M):
        for k in range(len(house)):
            dis[k] = min(dis[k], A[i][j][k])
    ans = min(ans, sum(dis))
print(ans)