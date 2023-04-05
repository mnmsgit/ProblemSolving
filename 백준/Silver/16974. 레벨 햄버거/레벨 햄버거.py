import sys

N, X = map(int, sys.stdin.readline().split())


bnp = [0] * (N+1)
p = [0] * (N+1)
bnp[0] = 1
p[0] = 1
for i in range(1,N):
    bnp[i] = 2 * bnp[i-1] + 3
    p[i] = 2 * p[i-1] + 1


def d_c(n, level, ans):
    if not level:
        return 1
    if n <=1:
        return 0
    mid = 2 + bnp[level-1]
    if mid > n:
        ans = d_c(n-1,level-1,ans)
    elif mid < n:
        ans = ans + p[level-1] + 1 + d_c(n-mid,level-1,ans)
    else:
        ans = ans + p[level-1] + 1
    return ans


print(d_c(X,N,0))
