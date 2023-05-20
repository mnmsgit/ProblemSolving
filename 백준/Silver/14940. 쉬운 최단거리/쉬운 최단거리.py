import sys
from collections import deque
n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split()))for i in range(n)]
ans = [[0 for _ in range(m)] for __ in range(n)]

start_x, start_y = 0, 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    for j in range(m):
        if graph[i][j] ==2:
            start_x = j
            start_y = i


def bfs(x, y):
    queue = deque()
    ans[y][x] =0
    queue.append((x,y))
    while queue:
        cur_x, cur_y = queue.popleft()
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]
            if new_x in range(m) and new_y in range(n):
                if graph[new_y][new_x] == 1 and not ans[new_y][new_x]:
                    ans[new_y][new_x] = ans[cur_y][cur_x] +1
                    queue.append((new_x,new_y))



bfs(start_x, start_y)

for i in range(n):
    for j in range(m):
        if not ans[i][j]:
            if graph[i][j] == 1:
                print(-1, end= " ")
            else:
                print(ans[i][j], end=" ")
        else:
            print(ans[i][j], end= " ")
    print()
