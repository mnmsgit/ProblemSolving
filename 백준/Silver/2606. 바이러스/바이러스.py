"""
딕셔너리를 이용해 푸는 그래프 이론 문제
큐를 이용해 문제의 조건의 맞는 경우를 빠지지 않고 찾는데 이용함

+
23/6/29 재체점 issue로 수정
dictionary 사용 시 get 내장함수 사용 하여 key error exception 방지 ,bfs 풀이에서 dfs 풀이로 바꿈(둘 다 가능)
"""
import sys
input = sys.stdin.readline

N = int(input())
pairs = int(input())
graph = {}
visited = [False for i in range(N+1)]

for i in range(pairs):
    a, b = map(int, input().split())
    # key error를 피하기 위해 dictionary의 get 메서드 사용
    graph[a] = graph.get(a, []) + [b]
    graph[b] = graph.get(b, []) + [a]

ans = 0
visited[1] = True
# stack for dfs
stack = [1]

while stack:
    node = stack.pop()
    neighbors = graph.get(node)
    if neighbors is not None:
        for neighbor in neighbors:
            if not visited[neighbor]:
                ans += 1
                stack.append(neighbor)
                visited[neighbor] = True

print(ans)
