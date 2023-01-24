import sys
T = int(sys.stdin.readline())
for _ in range(T):
    items = int(sys.stdin.readline())
    item = [[], []]
    for i in range(2):
        item[i] = list(map(int,sys.stdin.readline().split()))
    dp = [[0,0]for _ in range(items)]
    dp[0][0] = item[0][0]
    dp[0][1] = item[1][0]
    for i in range(1,items):
        if i ==1:
            dp[i][0] = dp[i-1][1] + item[0][i]
            dp[i][1] = dp[i-1][0] + item[1][i]
        else:
            dp[i][0] = max(max(dp[i-2])+item[0][i],dp[i-1][1] + item[0][i])
            dp[i][1] = max(max(dp[i - 2]) + item[1][i], dp[i - 1][0] + item[1][i])
    print(max(dp[items-1]))

