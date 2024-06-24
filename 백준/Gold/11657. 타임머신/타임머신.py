import sys
INF = sys.maxsize
# Case 1: Negative cycle exists

# Case 2: Cannot reach destination

# Case 3 : Otherwise
N, M = map(int, sys.stdin.readline().split())
edges = []

# Graph
for i in range(M):
    # src, dst, cost
    A, B, C = map(int, sys.stdin.readline().split())
    edges.append((A, B, C))

# Start == 1
distance = [INF] * (N+1)
distance[1] = 0

# Bellman ford -> D[w] = min(D[v], + c[v][w])
for i in range(N):
    for start, dst, cost in edges:
        if distance[start] != INF and distance[dst] > distance[start] + cost:
            distance[dst] = distance[start] + cost
            # Case 1: Negative cycle exists
            if i == N-1:
                print(-1)
                exit(0)


for dis in distance[2:]:
    if dis == INF:
        # Case 2: Cannot reach destination
        print(-1)
    else:
        # Case 3 : Otherwise
        print(dis)

