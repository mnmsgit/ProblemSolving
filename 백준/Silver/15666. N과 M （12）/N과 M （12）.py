import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr = list(set(arr))
arr.sort()


def backtracking(li):
    if len(li) == M:
        print(*li)
        return
    for i in range(len(arr)):
        if len(li) == 0 or li[-1] <= arr[i]:
            li.append(arr[i])
            backtracking(li)
            li.pop()


backtracking([])
