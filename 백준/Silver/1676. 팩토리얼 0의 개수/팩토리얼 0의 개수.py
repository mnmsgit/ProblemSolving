import sys
N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
for i in range(N+1):
    if i < 3:
        dp[i] = 1
    else:
        dp[i] = dp[i-1] * i
ans = 0
fac = dp[N]
while True:
    if fac % 10:
        break
    else:
        ans += 1
        fac //= 10
print(ans)