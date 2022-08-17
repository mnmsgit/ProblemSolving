"""
그래프를 활용한 탐색 기초문제
bfs dfs 어느 것을 활용해도 가능함
"""
import sys
from collections import deque


def bfs(arr, x, y):
    arr[y][x] = 0
    queue = deque()
    queue.append((x, y))
    vector_x = [1, 0, -1, 0]
    vector_y = [0, 1, 0, -1]
    while queue:
        node = queue.popleft()
        for v in range(4):
            xn = node[0] + vector_x[v]
            yn = node[1] + vector_y[v]
            if graph[yn][xn]:
                queue.append((xn, yn))
                arr[yn][xn] = 0
    return 1


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(M+2)] for _ in range(N+2)]
    ans = 0
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        graph[Y+1][X+1] = 1
    for i in range(1, N+1):
        for j in range(1, M+1):
            if graph[i][j]:
                ans += bfs(graph, j, i)
    print(ans)
