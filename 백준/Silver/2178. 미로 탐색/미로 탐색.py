"""
1.bfs를 사용한 이유: 전체 탐색 이면서 최단거리를 구하기 때문 2. 미로 배열을 미로보다 크게 잡은 이유: index error 를 방지하기 위함(0은 갈수없는 곳 이므로 벽도 0으로 처리)
bfs로 구한 최단경로가 최단경로인 이유: 트리에서 최단경로가 아닌 경우는 이미 visited한 경우이기 때문에 제거됨
"""
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
    vectors = [[1, 0], [0, 1], [-1, 0], [0, -1]]   # x,y좌표가 나아갈 수 있는 방향을 저장한 배열
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

