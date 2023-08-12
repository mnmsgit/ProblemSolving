import sys

loop = 1
while True:
    size = int(sys.stdin.readline())
    if not size:
        break
    graph = [[]for _ in range(size)]
    for i in range(size):
        graph[i] = list(map(int,sys.stdin.readline().split()))
    ans = -5000000
    # case 1
    for row in range(size):
        for col in range(size-3):
            temp = graph[row][col] + graph[row][col+1] + graph[row][col+2] + graph[row][col+3]
            ans = max(ans, temp)
    for row in range(size-3):
        for col in range(size):
            temp = graph[row][col] + graph[row+1][col] + graph[row+2][col] + graph[row+3][col]
            ans = max(ans, temp)
    # case 2
    for row in range(size-1):
        for col in range(size-2):
            temp = graph[row][col] + graph[row][col+1] + graph[row+1][col+1] + graph[row+1][col+2]
            ans = max(ans, temp)
    for row in range(size-2):
        for col in range(size-1):
            temp = graph[row+1][col] + graph[row+2][col] + graph[row+1][col+1] + graph[row][col+1]
            ans = max(ans, temp)
    # case 3
    for row in range(size-1):
        for col in range(size-2):
            temp = graph[row][col] + graph[row][col+1] + graph[row][col+2] + graph[row+1][col+2]
            ans = max(ans, temp)
            temp = graph[row][col] + graph[row+1][col] + graph[row+1][col+1] + graph[row+1][col+2]
            ans = max(ans, temp)
    for row in range(size-2):
        for col in range(size-1):
            temp = graph[row][col+1] + graph[row+1][col+1] + graph[row+2][col+1] + graph[row+2][col]
            ans = max(ans, temp)
            temp = graph[row][col] + graph[row+1][col] + graph[row+2][col] + graph[row][col+1]
            ans = max(ans, temp)
    # case 4
    for row in range(size-1):
        for col in range(size-2):
            temp = graph[row][col] + graph[row][col+1] + graph[row][col+2] + graph[row+1][col+1]
            ans = max(ans, temp)
            temp = graph[row+1][col] + graph[row+1][col+1] + graph[row+1][col+2] + graph[row][col+1]
            ans = max(ans, temp)
    for row in range(size-2):
        for col in range(size-1):
            temp = graph[row][col] + graph[row+1][col] + graph[row+2][col] + graph[row+1][col+1]
            ans = max(ans, temp)
            temp = graph[row+1][col] + graph[row][col+1] + graph[row+1][col+1] + graph[row+2][col+1]
            ans = max(ans, temp)
    # case 5
    for row in range(size-1):
        for col in range(size-1):
            temp = graph[row][col] + graph[row][col+1] + graph[row+1][col] + graph[row+1][col+1]
            ans = max(ans, temp)
    print(loop,end="")
    print(". ",end="")
    print(ans,end="\n")
    loop += 1
