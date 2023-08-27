import sys


def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, node1, node2):
    root_a = find(parent, node1)
    root_b = find(parent, node2)

    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b


V, E = map(int,sys.stdin.readline().split())
parent = [0] * (V+1)
edges = []
result =0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, V + 1):
    parent[i] = i

for i in range(E):
    a, b, c = map(int,sys.stdin.readline().split())
    # 인접행렬 대신 연결 그래프로 표현 (value,목적지)
    edges.append((c,a,b))

edges.sort()
for edge in edges:
    c, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함(=연결한다.)
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += c
print(result)