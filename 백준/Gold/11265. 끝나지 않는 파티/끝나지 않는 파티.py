import sys
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    if C >= graph[A-1][B-1]:
        print("Enjoy other party")
    else:
        print("Stay here")
