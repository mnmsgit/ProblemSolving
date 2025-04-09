
N = int(input())

l = int(input())

graph =[[]for _ in range(N+1)]
visited = [False for _ in range(N+1)]

def dfs(node):
    global visited
    visited[node] = True
    for near in graph[node]:
        if not visited[near]:
            dfs(near)
    return

for _ in range(l):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)

print(visited.count(True)-1)
