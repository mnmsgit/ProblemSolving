# dp 사용 이유: 1. 최소값 구하는 문제 2. 부르트포스 사용하기에 경우가 많음 => dp 고려
# i 번째의 최솟값을 반복적으로 사용 + 최적 부분 구조를 구해야함 -> dp 사용 확신
# dp 테이블이 1차원 배열이라고 가정하고 풀어서 헤멘 문제
# dp 가 n차원이어도 n이 아주 크지 않으면 시간,공간복잡도 별로 안높다. 변수 개수 만큼 생각하는게 일반적


import sys

N = int(sys.stdin.readline())
price = [[]for i in range(N)]
for i in range(N):
    r,g,b = map(int,sys.stdin.readline().split())
    price[i] = [r,g,b]

case = [(1,2),(0,2),(0,1)]

dp = [[-1,-1,-1] for _ in range(N)]
dp[0] = price[0]
for i in range(1,N):
    for j in range(3):
        dp[i][j] = price[i][j] + min(dp[i-1][case[j][0]], dp[i-1][case[j][1]])
print(min(dp[N-1]))
