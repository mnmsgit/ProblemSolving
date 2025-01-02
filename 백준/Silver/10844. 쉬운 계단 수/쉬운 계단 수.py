import sys

input = sys.stdin.readline

N = int(input())

str_n = str(N)

# 첫 숫자와 나머지 분리 필요
# 같은 문제의 반복 -> 4번째 숫자가 5인 경우: 3번째가 4인 경우 + 3번째가 6인 경우(0,9는 예외)

dp = [[0 for _ in range(10)]for __ in range(N+1)]

# 첫번째 자리 처리

for num in range(1,10):
    dp[1][num] = 1

# 두번째 이후 자리

for index in range(1,N+1):
    for num in range(10):
        if 0 < num < 9:
            dp[index][num] += dp[index - 1][num - 1]
            dp[index][num] += dp[index - 1][num + 1]
        if num == 0:
            dp[index][num] += dp[index - 1][num + 1]
        if num == 9:
            dp[index][num] += dp[index - 1][num - 1]

print(sum(dp[N])%1000000000)