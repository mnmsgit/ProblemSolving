# backtracking 대표 문제 n,m(5)
# 방문한 적이 없는 노드는 담고 아니면 pass
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()
visited = [False for i in range(len(num_list))]


def backtracking(result):
    if len(result) == M:
        print(*result)
        return
    for i in range(len(num_list)):
        if not visited[i]:
            result.append(num_list[i])
            visited[i] = True
            # 재귀로 backtracking
            backtracking(result)
            # 탐색 완료한 경우
            visited[i] = False
            result.pop()


backtracking([])
