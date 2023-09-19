import sys
from collections import deque
dx = [1,-1,0,0,1,1,-1,-1]
dy = [0,0,1,-1,1,-1,1,-1]


def island(gra, x, y, vis):
    queue = deque()
    queue.append((x, y))

    while queue:
        now_x, now_y = queue.popleft()
        for i in range(8):
            new_x = now_x + dx[i]
            new_y = now_y + dy[i]
            if -1 < new_x < h and -1 < new_y < w and not visited[new_x][new_y] and gra[new_x][new_y] ==1:
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))





while True:
    w, h = map(int,sys.stdin.readline().split())
    if not w and not h:
        break
    graph = [[]for i in range(h)]
    visited = [[False for __ in range(w)] for _ in range(h)]
    for i in range(h):
        graph[i] = list(map(int,sys.stdin.readline().split()))
    count = 0
    for x in range(h):
        for y in range(w):
            if graph[x][y] ==1 and not visited[x][y]:
                count +=1
                island(graph,x,y,visited)

    print(count)
    