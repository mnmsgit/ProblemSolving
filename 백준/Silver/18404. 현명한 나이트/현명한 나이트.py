import sys
from collections import deque
INF = 10E9

N, M = map(int, sys.stdin.readline().split())
X, Y = map(int, sys.stdin.readline().split())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [-1,1,-2,2,-2,2,-1,1]

graph = [[INF for __ in range(N+1)] for _ in range(N+1)]

queue = deque()
graph[X][Y] = 0
queue.append((X,Y))

while queue:
    now_x, now_y = queue.popleft()
    for i in range(8):
        new_x = now_x + dx[i]
        new_y = now_y + dy[i]
        if 0<new_x<N+1 and 0<new_y<N+1 and graph[new_x][new_y] ==INF:
            graph[new_x][new_y] = graph[now_x][now_y] +1
            queue.append((new_x, new_y))


for i in range(M):
    a, b = map(int,sys.stdin.readline().split())
    print(graph[a][b])
    