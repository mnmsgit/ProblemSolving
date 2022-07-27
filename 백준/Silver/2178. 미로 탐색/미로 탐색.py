import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
maze = [[0 for _ in range(M+2)]for _ in range(N+2)]
graph = []

for i in range(1, N+1):
    line = sys.stdin.readline().strip()
    maze[i] = list(map(int, list('0'+line+'0')))

ans = 0


def bfs(x, y):
    count = 1
    visited = [[False for _ in range(M + 2)] for _ in range(N + 2)]
    queue = deque()
    queue.append([x, y, count])
    visited[x][y] = True
    vectors = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while queue:
        node = queue.popleft()
        count = node[2]
        for vector in vectors:
            row = node[0] + vector[0]
            col = node[1] + vector[1]
            if not visited[row][col] and maze[row][col]:
                queue.append([row, col, count+1])
                visited[row][col] = True
        if node[0] == N and node[1] == M:
            return count


print(bfs(1, 1))

