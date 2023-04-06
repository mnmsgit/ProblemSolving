import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr.insert(0, 0)
dp = [0] * (N+1)
largest_num = [0] * (N+1)

for i in range(1, N+1):
    if largest_num[dp[i-1]] < arr[i]:
        dp[i] = dp[i-1] + 1
        largest_num[dp[i]] = arr[i]
    else:
        dp[i] = dp[i-1]
        for k in range(1,dp[i-1]+1):
            if largest_num[k] >= arr[i]:
                largest_num[k] = arr[i]
                break

print(dp[N])
