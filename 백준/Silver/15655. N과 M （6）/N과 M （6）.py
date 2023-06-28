import sys

N, M = map(int ,sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()


def backtracking(arr):
    if len(arr) == M:
        print(*arr)
        return
    for num in num_list:
        if num not in arr and (len(arr) == 0 or arr[-1] < num):
            arr.append(num)
            backtracking(arr)
            arr.pop()


backtracking([])

