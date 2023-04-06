# 다이나믹 프로그래밍 문제
# 증가하는 경우 배열을 2개 사용해 하나는 가장 긴 증가하는 부분 수열의 길이, 하나는 증가하는 부분수열의 값을 변수로 사용
# 증가하는경우 dp테이블을 i-1에서 1만큼 증가시키며 증가하는 부분수열의 값 갱신 아닌경우 증가하는 부분수열의 값에서 arr[i]가 들어갈 곳을 찾아 갱신
import sys

N = int(sys.stdin.readline())

arr = list(map(int,sys.stdin.readline().split()))
arr.insert(0, 0)
dp = [0] * (N+1)  # dp 는 결과값 테이블
largest_num = [0] * (N+1) # 증가하는 수열의 i번째 값

for i in range(1, N+1):
    # 증가하는 경우
    if largest_num[dp[i-1]] < arr[i]:
        dp[i] = dp[i-1] + 1
        largest_num[dp[i]] = arr[i]
    # 아닌 경우
    else:
        dp[i] = dp[i-1]
        for k in range(1, dp[i-1]+1):
            if largest_num[k] >= arr[i]:
                largest_num[k] = arr[i]
                break

print(dp[N])
