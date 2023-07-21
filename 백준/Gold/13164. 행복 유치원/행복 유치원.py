import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
diff = []

for i in range(N-1):
    diff.append(arr[i+1]-arr[i])

diff.sort(reverse=True)
diff = diff[K-1:]
ans = sum(diff)
print(ans)
