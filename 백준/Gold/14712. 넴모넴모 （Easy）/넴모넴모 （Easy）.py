import sys
N, M = map(int, sys.stdin.readline().split())

count = 0
graph = [[False for i in range(M+1)] for _ in range(N+1)]

def backtracking(position):
    global count
    if position == N *M:
        count +=1
        return
    pos_x = position // M +1
    pos_y = position % M +1

    # 넴모를 안 담는 경우
    backtracking(position +1)
    ## 넴모를 담을 수 있고 담는 경우
    if not graph[pos_x-1][pos_y-1] or not graph[pos_x-1][pos_y] or not graph[pos_x][pos_y-1]:
        #넴모 담고 dfs
        graph[pos_x][pos_y] = True
        backtracking(position + 1)
        # backtrack되는 경우 다시 넴모 빼기
        graph[pos_x][pos_y] = False


backtracking(0)
print(count)

