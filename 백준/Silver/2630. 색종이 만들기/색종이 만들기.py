import sys

N = int(sys.stdin.readline())
graph = [[]for i in range(N)]

for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().split()))
ans = [0, 0]


def search(start, size): # 시작점과 크기
    color = graph[start[0]][start[1]]
    for i in range(size):
        for j in range(size):
            new_x = start[0] + i
            new_y = start[1] + j
            if graph[new_x][new_y] != color:
                search(start, size//2)
                search((start[0], start[1] + size//2), size//2)
                search((start[0] + size//2, start[1]), size//2)
                search((start[0] + size//2, start[1] + size//2), size//2)
                return
    ans[color] += 1


search((0,0),N)
print(ans[0])
print(ans[1])
