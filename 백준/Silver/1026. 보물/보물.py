import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
ans = 0

for i in range(N):
    ans += A[i]*B[i]
print(ans)
