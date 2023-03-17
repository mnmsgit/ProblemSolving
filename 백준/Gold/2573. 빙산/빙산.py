import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
graph = [[]for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))


def melting():
    con = False
    dis_graph = [[0 for j in range(M)]for i in range(N)]
    for i in range(1, N-1):
        for j in range(1, M-1):
            if graph[i][j]:
                minus_count = 0
                for move in range(4):
                    new_x = i + dx[move]
                    new_y = j + dy[move]
                    if 0 <= new_x < N and 0 <= new_y <M:
                        if not graph[new_x][new_y]:
                            minus_count += 1
                            con = True
                dis_graph[i][j] = minus_count
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                con = True
            graph[i][j] = max(graph[i][j] - dis_graph[i][j], 0)
    return con


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        node = queue.popleft()
        for i in range(4):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if 0 <= new_x < N and 0<= new_y < M:
                if not visited[new_x][new_y] and graph[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x,new_y))
    return True


clock = 0
while True:
    cnt = 0
    visited = [[False for j in range(M)]for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] and not visited[i][j]:
                if bfs((i, j)):
                    cnt += 1
    if cnt > 1:
        print(clock)
        break
    if not melting():
        print(0)
        break
    clock += 1


