from collections import deque
import sys
N = int(sys.stdin.readline())
graph = [[]for _ in range(N)]
for i in range(N):
    line = sys.stdin.readline().split()
    for j in range(N):
        if line[j] == '1':
            graph[i].append(j)
for i in range(N):
    visited = [0 for _ in range(N)]
    queue = deque()
    queue.extend(graph[i])
    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = 1
        for element in graph[node]:
            if not visited[element]:
                visited[element] = 1
                queue.append(element)
    print(*visited)