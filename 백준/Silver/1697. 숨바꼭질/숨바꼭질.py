# BFS를 이용한 그래프 문제
# visited 배열을 -1 인경우로 대체 했으며 그래프에서 방문하지 않은 경우 범위 조건에 맞추어서 큐에 추가 하였다.
# 범위 조건을 문제가 허용하는 가장 큰 범위를 잡고 시작하고 줄이는 것이 더 안전한 방법인 것 같다.
import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
graph = [-1 for i in range(100001)]

queue = deque()
queue.append(N)
graph[N] = 0

while queue:
    node = queue.popleft()
    if node-1 > -1 and graph[node-1] == -1:
        graph[node-1] = graph[node] + 1
        queue.append(node-1)
    if node + 1 < 100001 and graph[node + 1] == -1:
        graph[node + 1] = graph[node] + 1
        queue.append(node + 1)
    if node * 2 < 100001 and graph[node * 2] == -1:
        graph[node * 2] = graph[node] + 1
        queue.append(node * 2)
print(graph[K])



