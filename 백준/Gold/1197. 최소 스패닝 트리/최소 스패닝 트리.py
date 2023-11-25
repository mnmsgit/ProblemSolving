import sys

V, E = map(int, sys.stdin.readline().split())


def find(parent,x):
    if parent[x] == x:
        return x
    parent[x] = find(parent,parent[x])
    return parent[x]


def union(parent,a,b):
    rootA = find(parent,a)
    rootB = find(parent,b)

    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB


parent = [i for i in range(V+1)]


edges = []

for _ in range(E):
    a, b, cost = map(int, sys.stdin.readline().split())
    edges.append((a, b, cost))

edges.sort(key=lambda x: x[2])

ans = 0
for a,b,cost in edges:
    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        ans += cost

print(ans)
