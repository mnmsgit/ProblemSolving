# 기본 n과 m에서 원소의 중복 입력 허용하며 출력 값에 같은 값이 있어도 되므로 처음 배열에서 set 이용하여 중복 제거
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
