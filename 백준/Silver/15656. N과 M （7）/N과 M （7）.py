import sys

N, M = map(int, sys.stdin.readline().split())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()


def backtracking(ans):
    if len(ans) == M:
        print(*ans)
        return
    for i in range(N):
        ans.append(arr[i])
        backtracking(ans)
        ans.pop()


backtracking([])
