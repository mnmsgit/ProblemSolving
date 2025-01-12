"""
1. 벽 3개 세우기 -> combination
2. 그래프 탐색 -> bfs
3. 안전 구역 구하기 -> count 0
"""
import copy
import sys
from copy import deepcopy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


n, m = map(int,input().split())

wall_candidate = []
virus = []

ans = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 벽 채우기
def make_wall(graph, walls):
    new_graph = deepcopy(graph)
    for wall_row, wall_col in walls:
        new_graph[wall_row][wall_col] = 1
    return new_graph


def bfs(graph):
    queue = deque()
    safe_zone = 0
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 2:
                queue.append((row,col))

    while queue:
        node = queue.popleft()
        for i in range(4):
            new_row = node[0] + dx[i]
            new_col = node[1] + dy[i]
            if 0 <= new_row < n and 0 <= new_col < m:
                if graph[new_row][new_col] == 0:
                    graph[new_row][new_col] = 1
                    queue.append((new_row, new_col))
    for row in range(n):
        for col in range(m):
            if graph[row][col] == 0:
                safe_zone += 1
    return safe_zone





# 그래프 생성
lab_graph = [[]for _ in range(n)]
for i in range(n):
    lab_graph[i] = list(map(int, input().split()))

# 벽 후보지, 바이러스 업데이트
for i in range(n):
    for j in range(m):
        if lab_graph[i][j] == 0:
            wall_candidate.append((i, j))
            virus.append((i, j))


# 벽 후보지 중 벽을 결정
for wall_list in combinations(wall_candidate,3):
    graph_with_wall = make_wall(lab_graph, wall_list)

    # 그래프 탐색
    ans = max(ans,bfs(graph_with_wall))

print(ans)



