"""
bitmask + dp
"""

def tsp(n, w):
    INF = float('inf')
    dp = [[INF] * n for _ in range(1 << n)]

    # 출발지 초기화
    dp[1][0] = 0  # 0번 도시에서 시작, 0번 도시는 방문했다고 표시

    # 모든 상태를 순회
    for visited in range(1 << n):
        for current in range(n):
            if not (visited & (1 << current)):  # current 도시가 방문되지 않았으면 continue
                continue
            for next_city in range(n):
                if visited & (1 << next_city) or w[current][next_city] == 0:
                    continue
                dp[visited | (1 << next_city)][next_city] = min(
                    dp[visited | (1 << next_city)][next_city],
                    dp[visited][current] + w[current][next_city]
                )

    min_cost = INF
    for city in range(1, n):
        if w[city][0] != 0:
            min_cost = min(min_cost, dp[(1 << n) - 1][city] + w[city][0])

    return min_cost


n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

print(tsp(n, w))
