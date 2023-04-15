# Remind:1차원 배열로 풀기
import sys


def f1(a):
    dp = [[0, 0]for _ in range(a+1)]
    if a == 0:
        return [1, 0]
    elif a == 1:
        return [0, 1]
    else:
        dp[0] = [1, 0]
        dp[1] = [0, 1]
        for i in range(2, a + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]
        return [dp[a][0], dp[a][1]]


T = int(sys.stdin.readline())
for _ in range(T):
    print(*f1(int(sys.stdin.readline())))
