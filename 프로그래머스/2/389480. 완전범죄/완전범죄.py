def solution(info, n, m):
    # dp[a][b] = 물건을 일부(또는 전부) 훔친 후
    # A 흔적 합이 a, B 흔적 합이 b가 가능한지 여부
    dp = [[False] * m for _ in range(n)]
    dp[0][0] = True

    for ai, bi in info:
        next_dp = [[False] * m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                # 1) A가 i번 물건 훔치기
                na = a + ai
                if na < n:
                    next_dp[na][b] = True
                # 2) B가 i번 물건 훔치기
                nb = b + bi
                if nb < m:
                    next_dp[a][nb] = True
        dp = next_dp

    # 가능한 상태 중 A 합(a)의 최솟값 찾기
    answer = float('inf')
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                answer = min(answer, a)

    return answer if answer != float('inf') else -1
