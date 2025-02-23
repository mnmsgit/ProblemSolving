import sys


N, M, B = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N)]

for i in range(N):
    graph[i] = list(map(int, sys.stdin.readline().split()))


height = -1

needed_time = 10E10

for h in range(257):
    needed_block, removal_block, needed_block_amount, removal_block_amount = 0, 0, 0, 0
    for row in range(N):
        for col in range(M):
            if h > graph[row][col]:
                needed_block += 1
                needed_block_amount += h - graph[row][col]
            elif h < graph[row][col]:
                removal_block += 1
                removal_block_amount += graph[row][col] - h

    if B + removal_block_amount < needed_block_amount:
        break

    if needed_block_amount + removal_block_amount * 2 <= needed_time:
        needed_time = needed_block_amount + removal_block_amount * 2
        height = h
print(needed_time, height)


