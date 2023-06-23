# backtracking 대표 문제
# iteration 라이브러리 와 not in 메소드를 사용하지 않아 python에 종속 되지 않게 풀이
# 오름차순 만족하는 경우 재귀를 통해 탐색 , 실패한 경우 backtrack
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [i for i in range(1, N+1)]
visited = [False for i in range(N+1)]


def backtracking(result):
    if len(result) == M:
        print(*result)
        return
    for num in num_list:
        if not visited[num] and (not len(result) or result[-1] < num):
            result.append(num)
            # 재귀로 backtracking
            backtracking(result)
            # return 조건을 만족 못 한 경우
            result.pop()


backtracking([])
