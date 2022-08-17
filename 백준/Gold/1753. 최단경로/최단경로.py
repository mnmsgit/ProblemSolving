import sys
import heapq
INF = sys.maxsize
V, E = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())
graph = [[]for _ in range(V+1)]
distance = [INF for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))


def dijkstra(start):
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if distance[now] < wei:
            continue
        for wn, next_node in graph[now]:
            next_wei = wei + wn
            if next_wei < distance[next_node]:
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))


dijkstra(s)

for dis in distance[1:]:
    if dis == INF:
        print("INF")
    else:
        print(dis)