# dp 임을 찾아내기 까지가 어려운 문제
# 이천수는 조건 1,2 에 따라 피보나치 처럼 증가하므로 점화식이 피보나치와 같게 나옴
import sys
n = int(sys.stdin.readline())
memo = [0 for _ in range(n+1)]
memo[0], memo[1] = 1, 1
for i in range(2, n):
    memo[i] = memo[i-1] + memo[i-2]
print(memo[n-1])
