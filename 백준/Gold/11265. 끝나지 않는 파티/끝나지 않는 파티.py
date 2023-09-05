import sys
INF = 10000000000
N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split()))for _ in range(N)]
distance = [[INF for __ in range(N)]for _ in range(N)]


def party(start, dist, time):
    return time >= graph[start][dist]


for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])


for i in range(M):
    A, B, C = map(int, sys.stdin.readline().split())
    if party(A-1, B-1, C):
        print("Enjoy other party")
    else:
        print("Stay here")
