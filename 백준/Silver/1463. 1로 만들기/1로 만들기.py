"""
dp를 이용한 기초적인 문제
dp 사용이유: 1. 최솟값 구하는 문제 2. 큰수로 먼저 나누는 것(그리디 알고리즘)이 최적의 방법이라고 생각했지만 10의 결과가 10 -> 9 -> 3 ->1 임에서
그리디 알고리즘을 사용할 수 없음을 생각
구현: 상향식(bottom-up)방식을 사용
"""
import sys
n = int(sys.stdin.readline())

dp = [0 for _ in range(n+1)]
for i in range(2, n+1):
    dp[i] = dp[i - 1] + 1
    if not i % 3:
        dp[i] = min(dp[i], dp[i//3]+1)
    if not i % 2:
        dp[i] = min(dp[i], dp[i//2]+1)
print(dp[n])


