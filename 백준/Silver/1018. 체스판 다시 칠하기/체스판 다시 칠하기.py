import sys

N, M = map(int, sys.stdin.readline().split())
board = [[]for _ in range(N)]
ans = []
for i in range(N):
    board[i] = list(sys.stdin.readline().strip())
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2:
                    if board[row][col] == 'W':
                        count += 1
                else:
                    if board[row][col] == 'B':
                        count += 1
        ans.append(min(count, 64-count))
print(min(ans))
