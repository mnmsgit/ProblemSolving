from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())


def find_sibling(N, K):
    visited = [-1] * 100001
    queue = deque()

    queue.append(N)
    visited[N] = 0

    while queue:
        current = queue.popleft()
        if current == K:
            return visited[current]

        if 0 <= 2 * current < 100001 and visited[2 * current] == -1:
            visited[2 * current] = visited[current]
            queue.appendleft(2 * current)

        for next_pos in [current - 1, current + 1]:
            if 0 <= next_pos < 100001 and visited[next_pos] == -1:
                visited[next_pos] = visited[current] + 1
                queue.append(next_pos)


print(find_sibling(N, K))

