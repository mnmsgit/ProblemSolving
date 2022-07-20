"""
변수가 3개인 dp 문제
함수 w의 값이 항상 0보다 큼을 이용해 메모지에이션을 이용한 하향식으로 풀이
점화식과 기저조건이 문제에 주어졌으며 구현만 할 수 있다면 풀 수 있는 문제이다.
"""
import sys
R = range(51)
dp = [[[0 for _ in R]for _ in R]for _ in R]


def w(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return 1
    if x > 20 or y > 20 or z > 20:
        if dp[20][20][20]:
            return dp[20][20][20]
        else:
            return w(20, 20, 20)
    if dp[x][y][z]:
        return dp[x][y][z]
    if x < y < z:
        dp[x][y][z] = w(x, y, z-1) + w(x, y-1, z-1) - w(x, y-1, z)
    else:
        dp[x][y][z] = w(x-1, y, z) + w(x-1, y-1, z) + w(x-1, y, z-1) - w(x-1, y-1, z-1)
    return dp[x][y][z]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

