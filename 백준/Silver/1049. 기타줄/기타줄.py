import sys

N, M = map(int, sys.stdin.readline().split())

arr1 = []
arr2 = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr1.append(a)
    arr2.append(b)

arr1.sort()
arr2.sort()
ans =0
if arr1[0] >= arr2[0]* 6:
    ans = arr2[0] * N
else:
    ans = arr1[0] * (N//6)
    ans += min(arr1[0], arr2[0] * (N % 6))
print(ans)