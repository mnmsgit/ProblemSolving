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
