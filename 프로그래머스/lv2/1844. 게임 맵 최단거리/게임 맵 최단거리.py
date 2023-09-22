from collections import deque

def solution(maps):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    n = len(maps)
    m = len(maps[0])
    count = [[0 for _ in range(m)] for __ in range(n)]
    count[0][0] =1
    queue = deque()
    queue.append((0,0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if -1<new_x<n and -1<new_y<m and maps[new_x][new_y] ==1 and count[new_x][new_y] ==0:
                count[new_x][new_y] = count[x][y]+1
                queue.append((new_x,new_y))
    
    if count[n-1][m-1]:
        return count[n-1][m-1]
    else:
        return -1
    
    return answer