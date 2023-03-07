import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [-1 for i in range(100001)]

queue = deque()
queue.append(N)
graph[N] = 0
while queue:
    node = queue.popleft()
    if node-1 > -1 and graph[node-1] == -1:
        graph[node-1] = graph[node] + 1
        queue.append(node-1)
    if node + 1 < 100001 and graph[node + 1] == -1:
        graph[node + 1] = graph[node] + 1
        queue.append(node + 1)
    if node * 2 < 100001 and graph[node * 2] == -1:
        graph[node * 2] = graph[node] + 1
        queue.append(node * 2)
print(graph[K])



