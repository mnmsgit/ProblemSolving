import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

indegree = [0] * (N+1)

graph = [[]for _ in range(N+1)]

for i in range(M):
    start, des = map(int, sys.stdin.readline().split())
    graph[start].append(des)
    indegree[des] += 1
queue = deque()
ans = []
for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
while queue:
    node = queue.popleft()
    ans.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            queue.append(next_node)

print(*ans)


