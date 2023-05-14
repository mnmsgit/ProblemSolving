# 모든 경로의 최단거리 이므로 플로이드-워셜 알고리즘 이용.
# 인접행렬 이용, 자신과 자신과의 거리는 0이고 간선이 양방향이므로 graph[a][b] = graph[b][a] = l 이다.
# k가 플로이드 워셜 알고리즘 내에서 구분자 역할 
# 이후 최대 가치를 얻는 출발점 계산
import sys

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int,sys.stdin.readline().split()))
items.insert(0,0) # index를 맞춰주기 위함
INF = sys.maxsize

graph = [[INF for _ in range(n+1)]for i in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0
for _ in range(r):
    a, b, l = map(int,sys.stdin.readline().split())
    graph[a][b] = l
    graph[b][a] = l

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans =0
for i in range(1,n+1):
    part = 0 # i 번 노드 에서의 아이템의 최대값
    for j in range(1,n+1):
        if graph[i][j] <= m:
            part += items[j]
    ans = max(ans,part)
print(ans)
