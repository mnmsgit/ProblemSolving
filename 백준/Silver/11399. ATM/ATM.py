import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = [0 for _ in range(N)]
time = 0
for i in range(N):
    element = 0
    for j in range(i+1):
        element += arr[j]
    ans[i] = element
print(sum(ans))
