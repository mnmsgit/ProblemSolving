import sys
import heapq

n, m, r = map(int, sys.stdin.readline().split())
items = list(map(int,sys.stdin.readline().split()))
items.insert(0,0) # index를 맞춰주기 위함
INF = sys.maxsize

graph = [[INF for _ in range(n+1)]for i in range(n+1)]

for i in range(1,n+1):
    graph[i][i] = 0
for _ in range(r):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a][b] = c
    graph[b][a] = c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

ans =0
for i in range(1,n+1):
    part = 0
    for j in range(1,n+1):
        if graph[i][j] <= m:
            part += items[j]
    ans = max(ans,part)
print(ans)

