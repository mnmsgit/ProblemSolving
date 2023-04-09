import sys

N = int(sys.stdin.readline())

item = [[0,0]]
for _ in range(N):
    item.append(list(map(int, input().split())))
dp = [[0 for _ in range(N+1)] for __ in range(N+1)]


for col in range(1,N+1):
    for row in range(col-1,0,-1):
        candi = sys.maxsize
        for k in range(row,col):
            value = dp[row][k] + dp[k+1][col] + item[row][0] * item[k][1] * item[col][1]
            candi = min(candi,value)
        dp[row][col] = candi

print(dp[1][N])

