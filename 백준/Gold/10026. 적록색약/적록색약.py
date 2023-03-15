import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[]for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

for i in range(N):
    graph[i] = list(sys.stdin.readline().strip())

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def normal_bfs(start):
    color = graph[start[0]][start[1]]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    while queue:
        node = queue.popleft()
        for i in range(4):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if 0 <= new_x < N and 0 <= new_y<N:
                if not visited[new_x][new_y] and graph[new_x][new_y] == color:
                    visited[new_x][new_y] = True
                    queue.append((new_x,new_y))
    return True


def colorblind_bfs(start):
    color = graph[start[0]][start[1]]
    if color == 'B':
        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = True
        while queue:
            node = queue.popleft()
            for i in range(4):
                new_x = node[0] + dx[i]
                new_y = node[1] + dy[i]
                if 0 <= new_x < N and 0 <= new_y<N:
                    if not visited[new_x][new_y] and graph[new_x][new_y] == color:
                        visited[new_x][new_y] = True
                        queue.append((new_x,new_y))
    else:
        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = True
        while queue:
            node = queue.popleft()
            for i in range(4):
                new_x = node[0] + dx[i]
                new_y = node[1] + dy[i]
                if 0 <= new_x < N and 0 <= new_y < N:
                    if not visited[new_x][new_y] and graph[new_x][new_y] != 'B':
                        visited[new_x][new_y] = True
                        queue.append((new_x, new_y))
    return True


norm = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            normal_bfs((i,j))
            norm +=1

visited = [[False for _ in range(N)] for _ in range(N)]

c_blind =0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            colorblind_bfs((i,j))
            c_blind +=1

print(norm,c_blind)