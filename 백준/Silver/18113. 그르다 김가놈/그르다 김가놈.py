import sys

N, K, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    kimbap = int(sys.stdin.readline().strip())
    if kimbap >= 2* K:
        kimbap -= 2* K
        arr.append(kimbap)
    elif kimbap >= K:
        kimbap -= K
        arr.append(kimbap)

start = 1
if len(arr) == 0:
    print(-1)
    exit(0)
end = max(arr)
ans = -1

while start <= end:
    mid = (start + end) // 2
    count = 0
    for element in arr:
        count += element // mid
    if count < M:
        end = mid -1
    else:
        ans = mid
        start = mid + 1

print(ans)

