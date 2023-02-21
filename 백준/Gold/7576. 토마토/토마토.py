import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(N)]
start = []
for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        if graph[i][j] == 1:
            start.append((i, j))


def bfs(start_arr):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    queue = deque(start_arr)
    while queue:
        x, y = queue.popleft()
        for z in range(4):
            new_x = x + dx[z]
            new_y = y + dy[z]
            if 0 <= new_x < N and 0 <= new_y < M:
                if graph[new_x][new_y] == 0:
                    graph[new_x][new_y] = graph[x][y] + 1
                    queue.append((new_x, new_y))


bfs(start)
ans = -1
anti_con = False
for i in range(N):
    ans = max(max(graph[i]), ans)
    if 0 in graph[i]:
        anti_con = True
if anti_con:
    print(-1)
else:
    print(ans -1)
