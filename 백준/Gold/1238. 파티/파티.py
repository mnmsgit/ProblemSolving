import heapq
import sys


N, M, x = map(int, sys.stdin.readline().split())
graph = {}
reverse_graph = {}

for i in range(1, M + 1):
    start, end, time = map(int, sys.stdin.readline().split())
    if start not in graph:
        graph[start] = []
    if end not in reverse_graph:
        reverse_graph[end] = []
    graph[start].append((end, time))
    reverse_graph[end].append((start, time))


def dijkstra(graph, start, n):
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


to_x = dijkstra(graph, x, N)
from_x = dijkstra(reverse_graph, x, N)

max_time = max(to_x[i] + from_x[i] for i in range(1, N + 1))

print(max_time)
