import sys

N, K = map(int, sys.stdin.readline().split())
err = N - K
if err <= 0:
    ans = 0
else:
    for i in range(K-1):
        n = 0
        while err >= 2**n-1:
            n += 1
        if n>0:
            err -= 2**(n-1)-1
    p = 0
    while err > 2**p-1:
        p += 1
    if p >0:
        err = 2**p-1 - err
    ans = err

print(ans)

