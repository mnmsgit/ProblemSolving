import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()
str1 = " " + str1
str2 = " " + str2
len1 = len(str1)
len2 = len(str2)

dp = [["" for _ in range(len2)] for _ in range(len1)]

for i in range(1, len1):
    letter1 = str1[i]
    for j in range(1, len2):
        letter2 = str2[j]
        if letter1 == letter2:
            dp[i][j] = dp[i-1][j-1] + letter1
        else:
            dp[i][j] = dp[i-1][j] if len(dp[i-1][j]) >= len(dp[i][j-1]) else dp[i][j-1]

print(len(dp[-1][-1]))
