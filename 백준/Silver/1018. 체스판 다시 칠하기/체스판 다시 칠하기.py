"""
전체 탐색(브루트 포스)를 이용한 기본문제
문제에서 4중 for문을 사용하지만 전체 경우의 수가 많지 않기 때문에 시간초과나지 않고 풀 수 있음
체스판 배열의 (행, 열)에서 (홀,홀)과 (짝,짝)이 같아야 하기 때문에 합이 짝수인 경우로 풀이
추가적으로 W,B로 시작하는 각각의 경우를 나눠서 계산하기 보다, 전체 경우(8*8)에서 하나의 경우를 빼고 둘중 작은 값을 기존 값과 비교해 구함
"""
import sys

N, M = map(int, sys.stdin.readline().split())
board = [[]for _ in range(N)]
ans = sys.maxsize
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
        ans = min(ans, min(count, 64-count))
print(ans)
