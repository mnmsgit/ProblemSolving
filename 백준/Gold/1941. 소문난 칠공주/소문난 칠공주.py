from collections import deque
from itertools import combinations

# 입력
board = [input().strip() for _ in range(5)]

# 5x5 좌표를 1차원 인덱스로 변환 (0~24)
positions = [(i // 5, i % 5) for i in range(25)]

answer = 0

def is_connected_and_valid(group):
    # group: 7개 인덱스
    visited = [False] * 7
    q = deque()
    q.append(0)
    visited[0] = True
    count = 1
    s_count = 0

    if board[positions[group[0]][0]][positions[group[0]][1]] == 'S':
        s_count += 1

    while q:
        now = q.popleft()
        r1, c1 = positions[group[now]]
        for i in range(7):
            if not visited[i]:
                r2, c2 = positions[group[i]]
                if abs(r1 - r2) + abs(c1 - c2) == 1:
                    visited[i] = True
                    q.append(i)
                    count += 1
                    if board[r2][c2] == 'S':
                        s_count += 1

    return count == 7 and s_count >= 4

# 25개 중 7개 조합 생성
for comb in combinations(range(25), 7):
    if is_connected_and_valid(comb):
        answer += 1

print(answer)
