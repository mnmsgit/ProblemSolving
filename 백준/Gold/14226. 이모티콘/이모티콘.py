from collections import deque

def bfs(n):
    queue = deque()
    queue.append((1,0))
    emoji[1][0] = 0
    while queue:
        s,c = queue.popleft()
        if emoji[s][s] == -1:
            emoji[s][s] = emoji[s][c] +1
            queue.append((s,s))
        if s+c <= n and emoji[s+c][c] == -1:
            queue.append((s+c,c))
            emoji[s+c][c] = emoji[s][c] +1
        if s-1 >= 0 and emoji[s-1][c] == -1:
            queue.append((s-1,c))
            emoji[s-1][c] = emoji[s][c] +1


if __name__ == '__main__':
    n = int(input())
    emoji = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    bfs(n)
    ans = -1
    for i in range(n+1):
        if emoji[n][i] != -1:
            if ans == -1 or ans > emoji[n][i]:
                ans = emoji[n][i]


    print(ans)