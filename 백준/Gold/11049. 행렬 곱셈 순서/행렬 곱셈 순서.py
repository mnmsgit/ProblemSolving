"""
dp의 대표적 예시인 CMM문제
자세한 내용은 첨부자료 참조
"""
import sys

N = int(sys.stdin.readline())

item = [[0,0]]
for _ in range(N):
    item.append(list(map(int, input().split())))
dp = [[0 for _ in range(N+1)] for __ in range(N+1)]


for col in range(1, N+1):
    for row in range(col-1,0,-1):
        candi = sys.maxsize    # 최솟값 갱신을 위해 가장 큰 값을로 둠
        for k in range(row,col):
            value = dp[row][k] + dp[k+1][col] + item[row][0] * item[k][1] * item[col][1]  # 점화식 k는 앞 행렬과 뒷 행렬을 나누는 역할
            candi = min(candi,value)
        dp[row][col] = candi

print(dp[1][N])

