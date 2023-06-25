# backtracking 대표 문제 n,m(4)
# python은 or 연산에서 앞의 연산이 true면 뒤의 booltype 확인 x (단축 평가, 대부분의 언어가 지원) -> index 오류 나지 않음
import sys

N, M = map(int, sys.stdin.readline().split())
num_list = [i for i in range(1, N+1)]
visited = [False for i in range(N+1)]


def backtracking(result):
    if len(result) == M:
        print(*result)
        return
    for num in num_list:
        if len(result) == 0 or result[-1] <= num:
            result.append(num)
            # 재귀로 backtracking
            backtracking(result)
            # return 조건을 만족 못 한 경우
            result.pop()


backtracking([])
