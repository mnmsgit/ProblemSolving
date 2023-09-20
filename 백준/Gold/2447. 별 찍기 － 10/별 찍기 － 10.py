import sys

N = int(sys.stdin.readline())
graph = [[" " for __ in range(N)]for _ in range(N)]


def drawing(x,y,size):
    if size == 3:
        for i in range(3):
            for j in range(3):
                if i ==1 and j ==1:
                    pass
                else:
                    graph[x+i][y+j] = "*"
        return
    next_size = size//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                pass
            else:
                drawing(x + i * next_size, y + j * next_size, next_size)


drawing(0,0,N)
for a in range(N):
    print("".join(graph[a]))
