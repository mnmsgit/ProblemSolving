import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())
graph = {}
for _ in range(m):
    line = sys.stdin.readline().strip().split()
    line = list(map(int, line))
    if len(line) == 2:
        if line[0] in graph:
            graph[line[0]].append(line[1])
        else:
            graph[line[0]] = [line[1]]
        if line[1] in graph:
            graph[line[1]].append(line[0])
        else:
            graph[line[1]] = [line[0]]
    else:
        graph[line[0]] = []

qu = []
ans = set()
qu.append(1)
ans.add(1)
while qu:
    p = qu.pop(0)
    for element in graph[p]:
        if element not in ans:
            qu.append(element)
            ans.add(element)
print(len(ans)-1)
