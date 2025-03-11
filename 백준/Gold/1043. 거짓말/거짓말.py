import sys
from collections import deque

input = sys.stdin.readline
queue = deque()
N, M = map(int, input().split())

know_truth = [False] * (N+1)
# graph[#사람] = [사람이 속해있는 그룹]
graph = [[] for _ in range(N+1)]
# groups[#그룹] = [그룹에 속해있는 사람]
groups = [[]for _ in range(M)]


know_people = list(map(int, input().split()))
know_people = know_people[1:]
for member in know_people:
    know_truth[member] = True
    queue.append(member)

for i in range(M):
    groups[i] = list(map(int,input().split()))[1:]
    for member in groups[i]:
        graph[member].append(i)

while queue:
    now = queue.popleft()
    for group in graph[now]:
        for member in groups[group]:
            if not know_truth[member]:
                know_truth[member] = True
                queue.append(member)

ans = 0
for group in groups:
    # 과장할 조건
    condition = True
    for member in group:
        if know_truth[member]:
            condition = False
    if condition:
        ans +=1

print(ans)


