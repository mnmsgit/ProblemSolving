import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
low = 0
high = max(arr)
while True:
    if low > high:
        print(high)
        break
    mid = (low + high)//2
    tree = 0
    for element in arr:
        if element > mid:
            tree += element - mid
    if tree == M:
        print(mid)
        break
    elif tree < M:
        high = mid - 1
    else:
        low = mid + 1

