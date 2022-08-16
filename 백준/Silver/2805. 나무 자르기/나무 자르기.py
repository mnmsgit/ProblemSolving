"""
이진탐색을 이용한 응용문제
이진 탐색을 써야한다고 생각하기 까지 오래걸림
입력값이 크기 때문에 O(N)으로도 시간초과가 뜨기 때문에 이진 탐색을 이용해 시간복잡도를 O(n*logn)으로 줄여서 해결함
+ 재귀로도 풀어봄직함
"""
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
low = 0
high = max(arr)
while low <= high:
    mid = (low + high)//2
    tree = 0
    for element in arr:
        if element > mid:
            tree += element - mid
    if tree < M:
        high = mid - 1
    else:
        low = mid + 1
print(high)

