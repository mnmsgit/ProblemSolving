import sys
dp = [[[0 for _ in range(51)]for _ in range(51)]for _ in range(51)]


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
        if not dp[x][y][z-1]:
            dp[x][y][z-1] = w(x, y, z-1)
        if not dp[x][y-1][z-1]:
            dp[x][y-1][z-1] = w(x, y-1, z-1)
        if not dp[x][y-1][z]:
            dp[x][y-1][z] = w(x, y-1, z)
        return dp[x][y][z-1] + dp[x][y-1][z-1] - dp[x][y-1][z]
    else:
        if not dp[x-1][y][z]:
            dp[x-1][y][z] = w(x-1, y, z)
        if not dp[x-1][y-1][z]:
            dp[x-1][y-1][z] = w(x-1, y-1, z)
        if not dp[x-1][y][z-1]:
            dp[x-1][y][z-1] = w(x-1, y, z-1)
        if not dp[x-1][y-1][z-1]:
            dp[x-1][y-1][z-1] = w(x-1, y-1, z-1)
        return dp[x-1][y][z] + dp[x-1][y-1][z] + dp[x-1][y][z-1] - dp[x-1][y-1][z-1]


while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a, b, c)}")

