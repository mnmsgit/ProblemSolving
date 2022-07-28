import sys
from collections import deque
N = int(sys.stdin.readline())
maze = [[0 for _ in range(N+2)]for _ in range(N+2)]
house = []


def house_bfs(x, y):
    count = 0
    vector = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = [[False for _ in range(N+1)] for _ in range(N+1)]
    queue = deque()
    queue.append([x, y])
    while queue:
        node = queue.popleft()
        count += 1
        x = node[0]
        y = node[1]
        maze[x][y] = 0
        for v in vector:
            x = node[0] + v[0]
            y = node[1] + v[1]
            if maze[x][y] and not visited[x][y]:
                queue.append([x, y])
                visited[x][y] = True
    return count


for i in range(1, N+1):
    maze[i] = list(map(int, "0"+sys.stdin.readline().strip()+"0"))

for i in range(1, N+1):
    for j in range(1, N+1):
        if maze[i][j]:
            house.append(house_bfs(i, j))
house.sort()
print(len(house))
print(*house, sep="\n")
