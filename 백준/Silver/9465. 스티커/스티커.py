# dp를 이용한 기본 문제
# 전 스티커를 꼭 선택하지 않아도 되는 경우만 조심해 풀면 되었다.
# dp 사용해야 겠다는 생각이 난 이유: 1. 최대값 2. brute force 는 위의 경우 때문에 경우가 너무 많이 발생.
# 3. 반복되는 과전 존재 (i번째의 1번째를 선택했을 때 최대값을 알면 메모지에이션를 이용해 반복적인 계산 X)

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
            dp[i][0] = max(dp[i-2][1], dp[i-1][1]) + item[0][i]
            dp[i][1] = max(dp[i-2][0], dp[i-1][0]) + item[1][i]
    print(max(dp[items-1]))

