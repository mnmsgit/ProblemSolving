import sys

n = int(sys.stdin.readline())
seq = list(map(int, sys.stdin.readline().split()))
dp = [[0 for _ in range(n)] for i in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if seq[i] == seq[i+1]:
        dp[i][i+1]=1
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j = i+2+cnt
        if seq[i]==seq[j] and dp[i+1][j-1]==1 :
            dp[i][j]=1

m = int(input())
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(dp[a-1][b-1])
    