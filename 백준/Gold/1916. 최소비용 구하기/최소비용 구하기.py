# 다익스트라 최단 경로 알고리즘을 이용한 문제
# 문제는 다익스트라 문제 그 자체
# 최소힙을 이용하여 시간 문제를 대폭 개선한 버전
# 최소힙 쓰는 부분부터의 과정을 이해하고 암기할 필요가 있다.
import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[]for _ in range(N+1)]
distance = [sys.maxsize] * (N+1)

for i in range(M):
    cur, dest, cost = map(int,sys.stdin.readline().split())
    graph[cur].append((dest, cost))
start, end = map(int,sys.stdin.readline().split())

q = []
heapq.heappush(q,(0, start))
distance[start] = 0
while q:
    dist, cur_node = heapq.heappop(q)
    if distance[cur_node] < dist:
        continue
    for dest, cost in graph[cur_node]:
        if distance[dest] > cost + dist:
            distance[dest] = cost + dist
            heapq.heappush(q, (cost + dist, dest))
print(distance[end])
