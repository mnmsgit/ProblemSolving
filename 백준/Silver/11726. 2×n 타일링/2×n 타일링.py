import sys

N = int(sys.stdin.readline())
b_c = [[0 for _ in range(N+1)] for __ in range(N+1)]
for i in range(N+1):
    b_c[i][0] = 1
for i in range(1,N+1):
    for j in range(1,i+1):
        if i ==j:
            b_c[i][j] =1
        else:
            b_c[i][j] = b_c[i-1][j-1] + b_c[i-1][j]

ans = 0
for i in range((N//2)+1):
    ans += (b_c[N-i][i]) % 10007
ans = ans % 10007

print(ans)
