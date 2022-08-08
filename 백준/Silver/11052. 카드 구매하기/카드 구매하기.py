import sys
N = int(sys.stdin.readline())
dp = [0 for _ in range(N+1)]
card = [0]
card.extend(list(map(int, sys.stdin.readline().split())))
for i in range(1, N+1):
    price = 0
    for j in range(1, (i//2)+1):
        price = max(price, dp[j] + dp[i-j])
    dp[i] = max(price, card[i])

print(dp[N])
