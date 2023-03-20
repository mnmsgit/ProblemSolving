# Divide and conquer 대표 문제
# D&C는 일반적으로 재귀적으로 풀며 그렇기 때문에 top-down 방식이다.
# 이 문제는  시간 줄이기 위한 목적이 아닌 D&C로 풀어야만 하는 문제 때문에
import sys

N = int(sys.stdin.readline())
graph = [[]for i in range(N)]

for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().split()))
ans = [0, 0]


def search(start, size): # 시작점과 크기
    color = graph[start[0]][start[1]]
    flag = True
    for i in range(size):
        for j in range(size):
            new_x = start[0] + i
            new_y = start[1] + j
            if graph[new_x][new_y] != color:
                flag = False
    if not flag:
        search(start, size // 2)
        search((start[0], start[1] + size // 2), size // 2)
        search((start[0] + size // 2, start[1]), size // 2)
        search((start[0] + size // 2, start[1] + size // 2), size // 2)
    else:
        ans[color] += 1


search((0,0),N)
print(ans[0])
print(ans[1])
