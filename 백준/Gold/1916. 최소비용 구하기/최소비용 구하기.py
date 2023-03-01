import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[]for _ in range(N+1)]
# visited = [False for _ in range(N+1)]
distance = [sys.maxsize] * (N+1)

for i in range(M):
    cur, dest, cost = map(int,sys.stdin.readline().split())
    graph[cur].append((dest, cost))
start, end = map(int,sys.stdin.readline().split())

q = []
heapq.heappush(q,(0, start))
distance[start] = 0
while q:
    dist, cur_node = heapq.heappop(q)
    if distance[cur_node] < dist:
        continue
    for dest, cost in graph[cur_node]:
        if distance[dest] > cost + dist:
            distance[dest] = cost + dist
            heapq.heappush(q, (cost + dist, dest))
print(distance[end])
