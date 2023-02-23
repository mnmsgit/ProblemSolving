import sys
from collections import deque


N, M, K, X = map(int, sys.stdin.readline().split())
ans = []
graph =[[]for i in range(N+1)]
visited = [-1] * (N+1)


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


def bfs(start,k):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        node = queue.popleft()
        for element in graph[node]:
            if visited[element] == -1:
                visited[element] = visited[node]+1
                queue.append(element)
                if visited[element] == k:
                    ans.append(element)
    return ans.sort()


bfs(X,K)

if ans:
    for city in ans:
        print(city)
else:
    print(-1)

