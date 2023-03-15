import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

graph = [[]for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(N):
    graph[i] = list(map(int, input().split()))


def bfs(start, rain):
    if graph[start[0]][start[1]] <= rain or visited[start[0]][start[1]]:
        return False
    visited[start[0]][start[1]] = True
    queue = deque()
    queue.append(start)
    while queue:
        node = queue.popleft()
        for i in range(4):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if 0<= new_x <N and 0<= new_y <N:
                if not visited[new_x][new_y] and graph[new_x][new_y] > rain:
                    visited[new_x][new_y] = True
                    queue.append((new_x,new_y))
    return True

ans = 0
for rains in range(0,100):
    count =0
    visited = [[False for _ in range(N)] for i in range(N)]
    for j in range(N):
        for k in range(N):
            if bfs((j,k),rains):
                count += 1
    ans = max(ans,count)
print(ans)

