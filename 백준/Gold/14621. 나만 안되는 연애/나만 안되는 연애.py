# MST(minimum spanning tree)이용한 문제
# 최소 거리라는 단어 때문에 다익스트라를 생각했으나 그림을 통해 MST가 더 적합함을 파악함
# graph를 인접행렬로, MST중 prim 알고리즘으로 고집해서 오래 걸린 문제
# kruskal 알고리즘과, 인접 리스트를 알아두어 유연성이 필요함
import sys
import heapq
INF = int(1e9)
N, M = map(int,sys.stdin.readline().split())
arr = list(sys.stdin.readline().strip().split())
man = [True for _ in range(N+1)]
for i in range(N):
    if arr[i] == "W":
        man[i+1] = False


adj = [[0 for __ in range(N+1)]for _ in range(N+1)]
for i in range(M):
    u, v, d = map(int, sys.stdin.readline().split())
    if man[u] != man[v]:
        adj[u][v] = d
        adj[v][u] = d
ans = INF


connected = [False for _ in range(N + 1)]
connected[0] = True
start = 1
queue = []
heapq.heappush(queue, (0, start))
sum_w = 0
while queue:
    weight, now = heapq.heappop(queue)
    if not connected[now]:
        sum_w += weight
        connected[now] = True
        for j in range(1,N+1):
            if adj[now][j] != 0 and not connected[j]:
                if adj[j][now] !=0 and adj[j][now]<adj[now][j]:
                    heapq.heappush(queue,(adj[j][now],j))
                else:
                    heapq.heappush(queue, (adj[now][j], j))

if False in connected:
    ans =- 1
else:
    ans = sum_w
print(ans)

