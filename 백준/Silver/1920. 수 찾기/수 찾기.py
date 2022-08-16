"""
이진탐색(binary Search)를 이용한 기본문제
구현을 해보는 문제
"""
import sys


def b_search(array, value, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if array[mid] == value:
        return True
    elif array[mid] > value:
        return b_search(array, value, low, mid-1)
    else:
        return b_search(array, value, mid+1, high)


N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
M = int(input())
ans = list(map(int, sys.stdin.readline().split()))
for element in ans:
    if b_search(arr, element, 0, N - 1):
        print(1)
    else:
        print(0)
