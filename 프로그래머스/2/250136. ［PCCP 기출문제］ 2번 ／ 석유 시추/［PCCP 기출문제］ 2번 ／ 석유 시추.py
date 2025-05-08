from collections import deque
def solution(land):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    col_size, row_size = len(land[0]), len(land)
    ans = [[] for _ in range(col_size)]
    visited = [[False for _ in range(col_size)] for __ in range(row_size)]
    for col in range(col_size):
        for row in range(row_size):
            if not visited[row][col] and land[row][col] == 1:
                trace_col = set()
                trace_col.add(col)
                visited[row][col] = True
                area = 1
                queue = deque()
                queue.append((row,col))
                while queue:
                    now_r, now_c = queue.popleft()
                    for i in range(4):
                        new_r, new_c = now_r + dx[i], now_c + dy[i]
                        if 0<=new_r<row_size and 0<=new_c<col_size:
                            if not visited[new_r][new_c] and land[new_r][new_c] == 1:
                                area +=1
                                visited[new_r][new_c] = True
                                queue.append((new_r,new_c))
                                trace_col.add(new_c)
                for c in trace_col:
                    ans[c].append(area)
                
                
    answer = -1
    for a in ans:
        answer = max(answer,sum(a))
    
    return answer