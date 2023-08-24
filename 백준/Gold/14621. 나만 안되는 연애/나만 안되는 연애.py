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
        if adj[u][v] != 0:
            d = min(d, adj[u][v])
        if adj[v][u] != 0:
            d = min(d, adj[v][u])
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
        for j in range(1, N+1):
            if adj[now][j] != 0:
                heapq.heappush(queue, (adj[now][j], j))

if False in connected:
    ans =- 1
else:
    ans = sum_w
print(ans)

