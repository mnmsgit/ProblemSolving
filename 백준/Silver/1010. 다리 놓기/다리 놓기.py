import sys
T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int,sys.stdin.readline().split())
    fac = [0 for _ in range(M+1)]
    for i in range(M+1):
        if i <= 1:
            fac[i] = 1
        else:
            fac[i] = fac[i-1] * i
    print(fac[M] // (fac[N] * fac[M - N]))
