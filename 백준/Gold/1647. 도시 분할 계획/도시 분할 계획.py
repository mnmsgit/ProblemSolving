# N개의 집, M개의 길, 양방향 , cost 존재
# 2개의 도시로 분할 -> 연결되어있고 적어도 1개의 집
import sys


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a_parent = find_parent(parent,a)
    b_parent = find_parent(parent,b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


N, M = map(int, sys.stdin.readline().split())

parent = [0] * (N+1)

for i in range(1,N+1):
    parent[i] = i

graph = []
result = 0

for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    graph.append((A,B,C))


graph.sort(key=lambda x: x[2])

max_cost = 0
for edge in graph:
    a, b, cost = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        max_cost = max(max_cost,cost)
result -= max_cost
print(result)

