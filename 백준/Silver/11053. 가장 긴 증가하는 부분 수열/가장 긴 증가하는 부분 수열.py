"""
dp를 이용한 기본적 문제
dp[n]항상 답일 것이라는 편견때문에 오래 걸린 문제
또한 test case가  N (1 ≤ N ≤ 1,000) 이므로 n2의 시간복잡도도 가능함.
"""
n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
