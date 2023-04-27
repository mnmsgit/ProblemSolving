import sys

N, K = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for i in range(N)]
ans = 0

for i in range(N-1, 0, -1):
    if K >= arr[i]:
        ans += K//arr[i]
        K = K % arr[i]
ans += K
print(ans)