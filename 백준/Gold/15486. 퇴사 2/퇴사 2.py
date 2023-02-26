# dp 대표 문제
# 1. 최댓값 구하기 2. 이전데이터 결과를 이용할 경우 반복된 연산 감소 -> dp사용 생각
# 테이블 체우기(메모지에이션) 즉, 상향식으로 문제 해결
# 전날까지의 최대량 + t일 걸린후 p값 을 더한 값을 채워 넣고 여러개가 채워질수 있으니 최댓값으로 채워 넣음 + 항상 전일의 수입 만큼은 벌 수 있으므로 dp[i-1]과도 비교
import sys

N = int(sys.stdin.readline())

T = [0]
P = [0]
dp = [0 for _ in range(N+1)]

for i in range(N):
    t, p = map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)

for i in range(1, N+1):
    if i + T[i]-1 <= N:
        dp[i + T[i]-1] = max(dp[i + T[i] - 1], dp[i-1] + P[i])
    dp[i] = max(dp[i], dp[i - 1])
print(dp[N])

