import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

num_set = set(arr)

M = int(input())
targets = list(map(int,input().split()))

ans = []

for target in targets:
    if target in num_set:
        ans.append(1)
    else:
        ans.append(0)
print(*ans)