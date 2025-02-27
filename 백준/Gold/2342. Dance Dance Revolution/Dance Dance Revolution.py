import sys

# cost
# 자기 자리: 1
# 가운데 -> 다른 곳: 2
# 다른 곳 -> 인접한 지점: 3
# 반대 편: 4
def cost(now_coord, dest_coord):
    if now_coord == dest_coord:
        return 1
    if now_coord == 0:
        return 2
    if abs(now_coord - dest_coord) == 2:
        return 4
    return 3

state = list(map(int, sys.stdin.readline().split()))
assert state[-1] == 0  
state.pop()            

state.insert(0, 0)

INF = 10**9
n = len(state)  # 실제 눌러야 할 횟수 + 1

# dp[turn][l][r]:
#   turn번째 지시( state[turn] )까지 처리한 뒤
#   왼발이 l, 오른발이 r에 위치했을 때의 최소 힘

dp = [[[INF]*5 for _ in range(5)]for _ in range(n)]

# 시작 상태: turn=0, (왼발=0, 오른발=0) 위치에서 비용 0
dp[0][0][0] = 0


for turn in range(1, n):
    dest = state[turn]        # 이번에 눌러야 할 지점
    prev_dest = state[turn-1] # 직전에 눌렀던 지점(연속 같은 지점 체크용)

    # 이전 단계의 (l, r) 모든 상태에 대해
    for l in range(5):
        for r in range(5):
            prev_cost = dp[turn-1][l][r]
            if prev_cost == INF:
                continue  # 도달 불가능 상태는 스킵

            #1.왼발 이동 
            # 1) 두 발이 같은 지점이 되면 불가능 => new_left == r 이면 안 됨
            # 2) 연속 같은 지점을 누르는 경우 (dest == prev_dest)면,
            #    직전에 누른 발이 '그 지점에 있던 발'이어야 함
            #    => 즉, dest == prev_dest 이고, l != prev_dest 라면 왼발은 그 지점 누를 수 없음
            if dest != r:
                if dest == prev_dest and l != prev_dest:
                    # 같은 지점 연속 누르기인데, 왼발이 해당 지점에 없었다면 불가능
                    pass
                else:
                    new_cost = prev_cost + cost(l, dest)
                    if new_cost < dp[turn][dest][r]:
                        dp[turn][dest][r] = new_cost

            # 2.오른발 이동
            if dest != l:
                if dest == prev_dest and r != prev_dest:
                    # 같은 지점 연속 누르기인데, 오른발이 그 지점에 없었다면 불가능
                    pass
                else:
                    new_cost = prev_cost + cost(r, dest)
                    if new_cost < dp[turn][l][dest]:
                        dp[turn][l][dest] = new_cost


answer = INF
for l in range(5):
    for r in range(5):
        if dp[n-1][l][r] < answer:
            answer = dp[n-1][l][r]

print(answer)
