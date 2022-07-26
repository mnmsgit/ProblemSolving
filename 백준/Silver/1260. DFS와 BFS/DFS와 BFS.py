"""
bfs 와 dfs를 구현 하는 기본적인 문제
graph를 2차원 배열로 둔 이유는 1~n 까지의 간선을 행으로 각 인접한 간선을 열로 두어 계산과 구현의 편리성을 위해 ㄷㅁ
dfs는 보통 함수의 재귀로, bfs는 보통 queue를 이용함.

"""

import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n+1)]
d_visited = [False for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
for arr in graph:
    arr.sort()


def dfs(start):
    print(start, end=" ")
    d_visited[start] = True
    for element in graph[start]:
        if not d_visited[element]:
            dfs(element)


def bfs(start):
    queue = deque()
    b_visited = [False for _ in range(n+1)]
    print(start, end=" ")
    b_visited[start] = True
    queue.extend(graph[start])
    while queue:
        node = queue.popleft()
        if not b_visited[node]:
            print(node, end=" ")
            b_visited[node] = True
            for element in graph[node]:
                if not b_visited[element]:
                    queue.append(element)


dfs(v)
print()
bfs(v)
