import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

ans = []
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
p_queue = []

# 그래프 생성
for i in range(M):
    start, des = map(int,sys.stdin.readline().split())
    indegree[des] += 1
    graph[start].append(des)

# 들어오는 간선이 0인 경우 큐에 추가

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(p_queue,i)

while p_queue:
    node = heapq.heappop(p_queue)
    ans.append(node)
    for next_node in graph[node]:
        indegree[next_node] -= 1
        if indegree[next_node] == 0:
            heapq.heappush(p_queue, next_node)

print(*ans)
