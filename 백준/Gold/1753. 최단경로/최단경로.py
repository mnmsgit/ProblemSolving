"""
다익스트라 알고리즘을 이용한 최단 거리 문제
가중치가 있는 경우 다익스트라 알고리즘과 우선순위 큐(heapq)를 이용 하면 시간복잡도를 줄여서 원하는 결과를 얻을 수 있음
첫 구현이라 주석을 통한 설명을 추가함
"""
import sys
import heapq
INF = sys.maxsize   # 무한대 거리를 의미
V, E = map(int, sys.stdin.readline().split())
s = int(sys.stdin.readline())
graph = [[]for _ in range(V+1)]     # 간선과 정점사이의 관계를 나타내는 그래프
distance = [INF for _ in range(V+1)]    # 해당 정점까지의 거리


def dijkstra(start):
    distance[start] = 0     # 시작하는 정점은 거리 0
    heap = []       # 시간복잡도를 줄이기 위해 우선순위 큐 이용
    heapq.heappush(heap, (0, start))    # 기존 큐에 넣듯 heapq에 추가
    while heap:
        wei, now = heapq.heappop(heap)
        if distance[now] < wei:     # 채워져 있는 배열과 비교해 이미 채워진 거리가 더 작을 경우 아래의 있을 인접노드 거리 계산을 무시(한 것으로 간주)
            continue
        for wn, next_node in graph[now]:    # 현재의 정점에서 간선으로 이어저있는 거리들에 대해 조사
            next_wei = wei + wn
            if next_wei < distance[next_node]:  # 이 때 추가된 가중치가 다음 정점에서의 값보다 작은 경우에만 heapq에 추가
                distance[next_node] = next_wei
                heapq.heappush(heap, (next_wei, next_node))
    return


for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((w, v))


dijkstra(s)

for dis in distance[1:]:
    if dis == INF:
        print("INF")
    else:
        print(dis)
