import sys
"""
시도 1 -> DP사용, 공간복잡도, 시간복잡도 모두 만족하지 못함. (답은 만족)
"""
#
# N, S = map(int, sys.stdin.readline().split())
#
# arr = list(map(int, sys.stdin.readline().split()))
# arr.insert(0, 0)
# dp = [[0 for _ in range(N+1)] for __ in range(N+1)]
#
# ans = 0
# for i in range(N+1):
#     for j in range(1, N+1):
#         dp[i][j] = dp[i-1][j] + arr[j]
#     if max(dp[i]) >= S:
#         ans = i+1
#         break
#
# print(ans)

"""
시도 2 -> 공간 복잡도 해결 -> 시간 복잡도 미해결
"""
# N, S = map(int, sys.stdin.readline().split())
#
# arr = list(map(int, sys.stdin.readline().split()))
# arr.insert(0, 0)
# dp = [0 for _ in range(N+1)]
#
# ans = 0
# for iter_count in range(1, N+1):
#     for i in reversed(range(1,N+1)):
#         dp[i] = dp[i-1] + arr[i]
#     if max(dp) >= S:
#         ans = iter_count
#         break
#
# print(ans)

"""
시도 3 -> 투포인터 활용한 풀이 : 시간복잡도 O(n)
"""

input = sys.stdin.readline

N, S = map(int, input().strip().split())
nums = list(map(int, input().strip().split()))

total = 0  # 부분합
start = 0
end = 0
min_len = 1e9

while True:
    # 현재 부분합이 찾고자하는 값보다 크거나 같다면
    if total >= S:
        min_len = min(min_len, end - start)  # 가장 짧은 길이 갱신
        total -= nums[start]
        start += 1

    # 현재 부분합이 찾고자하는 값보다 작다면
    elif total < S:
        if end == len(nums):  # 배열의 끝까지 탐색했다면 종료
            break
        total += nums[end]
        end += 1

if min_len == 1e9:
    print(0)
else:
    print(min_len)
    