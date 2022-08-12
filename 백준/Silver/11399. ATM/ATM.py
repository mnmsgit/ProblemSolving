import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
ans = []
time = 0
for i in range(N):
    if not i:
        ans.append(arr[i])
    else:
        ans.append(ans[i-1]+arr[i])
print(sum(ans))
