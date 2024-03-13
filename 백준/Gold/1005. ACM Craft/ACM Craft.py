import sys
from collections import deque
T = int(sys.stdin.readline())
INF = 10E9
for aa in range(T):
    N, K = map(int, sys.stdin.readline().split())
    D = list(map(int, sys.stdin.readline().split()))
    D.insert(0,0)
    graph = [[]for _ in range(N+1)]
    indegree = [0] * (N+1)
    queue = deque()
    distance = [0] * (N+1)
    for i in range(K):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        indegree[b] += 1
    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
            distance[i] = D[i]
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            indegree[next_node] -= 1
            if D[next_node] + distance[node] > distance[next_node]:
                distance[next_node] = D[next_node] + distance[node]
            if indegree[next_node] == 0:
                queue.append(next_node)
    W = int(sys.stdin.readline())
    print(distance[W])

