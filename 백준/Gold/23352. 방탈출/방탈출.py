import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
dx = [-1,1,0,0]
dy = [0,0,1,-1]
graph = [[]for i in range(N)]




def traversal(start):
    global N, M, dx, dy, graph
    visited = [[-1 for _ in range(M)]for __ in range(N)]
    end = start
    dist = -1
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 0
    while queue:
        node = queue.popleft()
        end = node
        for i in range(4):
            new_x = node[0] + dx[i]
            new_y = node[1] + dy[i]
            if -1 < new_x < N and -1 < new_y < M:
                if visited[new_x][new_y] == -1 and graph[new_x][new_y]:
                    visited[new_x][new_y] = visited[node[0]][node[1]] + 1
                    queue.append((new_x,new_y))
                    if dist < visited[new_x][new_y]:
                        dist = visited[new_x][new_y]
                        end = (new_x, new_y)
    return end, dist


for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))


ans = -1
temp =-1
s = [-1,-1]
d = [-1,-1]
for i in range(N):
    for j in range(M):
        if graph[i][j]:
            end_node, distance = traversal((i, j))
            if temp < distance:
                s = (i, j)
                d = end_node
                ans = graph[s[0]][s[1]] + graph[d[0]][d[1]]
                temp = distance
            elif temp == distance:
                s = (i, j)
                d = end_node
                ans = max(ans, graph[s[0]][s[1]] + graph[d[0]][d[1]])

if ans == -1:
    print(0)
else:
    print(ans)



