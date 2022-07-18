"""
dp(동적 계획법)을 이용한 문제
f(k)가 k원을 만들 수 있는 경우라 할 때 f(k-coin)이 f(k)와 같음을 이용해 풀이
top-down 보다는 down-top 방식으로 작은 값부터 채워나감
"""
import sys
n, k = map(int, sys.stdin.readline().split())
coins = []
memos = [0 for _ in range(k+1)]
memos[0] = 1
for _ in range(n):
    coins.append(int(sys.stdin.readline()))
for coin in coins:
    for i in range(coin, k+1):
        memos[i] += memos[i-coin]
print(memos[k])
