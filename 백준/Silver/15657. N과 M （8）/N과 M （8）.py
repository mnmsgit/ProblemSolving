import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()


def backtracking(ans):
    if len(ans) == M:
        print(*ans)
        return
    for element in arr:
        if len(ans) == 0 or ans[-1] <=element:
            ans.append(element)
            backtracking(ans)
            ans.pop()


backtracking([])
