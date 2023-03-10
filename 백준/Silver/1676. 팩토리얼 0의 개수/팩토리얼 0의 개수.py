# 다이나믹 프로그래밍을 이용한 문제
# 테이블 채우는 과정은 간단하지만 dp를 사용해야 한다는 생각이 들기까지 오랜 시간이 걸렸다.

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
