import sys
input = sys.stdin.readline

N = int(input())
cities = []

for _ in range(N):
    x, a = map(int, input().split())
    cities.append((x, a))

cities.sort()

total_population = sum(a for _, a in cities)

# 인구 절반지점
median_threshold = (total_population + 1) // 2
cumulative = 0
ans = sys.maxsize
for x, a in cities:
    cumulative += a
    if cumulative >= median_threshold:
        ans = x
        break

print(ans)