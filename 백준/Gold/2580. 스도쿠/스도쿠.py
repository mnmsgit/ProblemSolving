import sys
input = sys.stdin.readline

graph = [[]for i in range(9)]
row = [[True, False, False, False, False, False, False, False, False, False] for _ in range(9)]
col = [[True, False, False, False, False, False, False, False, False, False] for _ in range(9)]
square = [[True, False, False, False, False, False, False, False, False, False] for _ in range(9)]


def backtracking(idx):
    global graph
    global arr
    if idx == len(arr):
        for g in graph:
            print(" ".join(map(str, g)))
        sys.exit(0)
    x, y = arr[idx]
    for candidate in range(1,10):
        if not row[x][candidate] and not col[y][candidate] and not square[(x//3)*3 + (y//3)][candidate]:
            row[x][candidate] = True
            col[y][candidate] = True
            square[(x//3)*3 + (y//3)][candidate] = True
            graph[x][y] = candidate
            backtracking(idx+1)
            graph[x][y] = 0
            row[x][candidate] = False
            col[y][candidate] = False
            square[(x//3)*3 + (y//3)][candidate] = False


arr = []
for i in range(9):
    line = list(map(int,input().split()))
    graph[i] = line
    for j in range(9):
        value = line[j]
        if value:
            row[i][value] = True
            col[j][value] = True
            square[(i//3)*3 + (j//3)][value] = True
        else:
            arr.append((i,j))

backtracking(0)
