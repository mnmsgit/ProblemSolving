import sys
from collections import deque
N = int(sys.stdin.readline())
graph = [[0 for _ in range(N+2)]for _ in range(N+2)]
n1 = int(sys.stdin.readline())
for i in range(N+2):
    for j in range(N+2):
        if not i or i == N+1:
            graph[i][j] = -1
        if not j or j == N+1:
            graph[i][j] = -1
for _ in range(n1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 2
rotate = deque()
b = int(sys.stdin.readline())
for _ in range(b):
    a, b = sys.stdin.readline().rstrip().split()
    rotate.append([int(a), b])
game = True
time = 0
snake = deque()
snake.append([1, 1])
graph[1][1] = 1
vector = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d_r = 0
while game:
    time += 1
    head_col = snake[-1][0] + vector[d_r][0]
    head_row = snake[-1][1] + vector[d_r][1]
    # 게임 끝나는 조건 3개
    # if not head_col or not head_row:
    #     break
    # if head_col > N or head_row > N:
    #     break
    if graph[head_col][head_row] == 1 or graph[head_col][head_row] == -1:
        break
    # 게임 진행
    if graph[head_col][head_row] == 2:
        pass
    else:
        o = snake.popleft()
        graph[o[0]][o[1]] = 0
    graph[head_col][head_row] = 1
    snake.append([head_col, head_row])
    # 회전
    if rotate:
        if rotate[0][0] == time:
            if rotate[0][1] == 'D':
                d_r += 1
            else:
                d_r -= 1
                if d_r < 0:
                    d_r += 4
            d_r = d_r % 4
            rotate.popleft()
print(time)
    