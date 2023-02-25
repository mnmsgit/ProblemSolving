import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

result = 0
while low <= high:
    mid = (low + high)//2
    cut = 0
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    if cut < M:
        high = mid - 1
    else:
        result = mid
        low = mid + 1
print(result)

