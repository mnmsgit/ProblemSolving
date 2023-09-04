import sys

R, C, T = map(int, sys.stdin.readline().split())

graph = [[]for i in range(R)]
conditioner = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
clockwise = 0
counter_clockwise = 0


def diffusion():
    global graph
    temp = [[0 for _ in range(C)]for __ in range(R)]
    for x in range(R):
        for y in range(C):
            if graph[x][y] > 0:
                diff_amount = graph[x][y] // 5
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if -1<new_x<R and -1<new_y<C and graph[new_x][new_y] !=-1:
                        temp[new_x][new_y] += diff_amount
                        graph[x][y] -= diff_amount
    for x in range(R):
        for y in range(C):
            graph[x][y] += temp[x][y]
    return


def conditioning():
    # counter-clockwise
    # down
    for i in reversed(range(1,counter_clockwise)):
        graph[i][0] = graph[i-1][0]
    # left
    for i in range(C-1):
        graph[0][i] = graph[0][i+1]
    # up
    for i in range(counter_clockwise):
        graph[i][C-1] = graph[i+1][C-1]
    # right
    for i in reversed(range(2, C)):
        graph[counter_clockwise][i] = graph[counter_clockwise][i-1]
    graph[counter_clockwise][1] = 0

    # clockwise
    # up
    for i in range(clockwise+1, R-1):
        graph[i][0] = graph[i+1][0]
    # left
    for i in range(C-1):
        graph[R-1][i] = graph[R-1][i+1]
    # down
    for i in reversed(range(clockwise+1, R)):
        graph[i][C-1] = graph[i-1][C-1]
    # right
    for i in reversed(range(2, C)):
        graph[clockwise][i] = graph[clockwise][i-1]
    graph[clockwise][1] = 0


def counting():
    ans = 2
    for i in range(R):
        ans += sum(graph[i])
    return ans


for i in range(R):
    graph[i] = list(map(int, sys.stdin.readline().split()))
    if graph[i][0] == -1:
        counter_clockwise = i-1
        clockwise = i

for _ in range(T):
    diffusion()
    conditioning()

print(counting())
