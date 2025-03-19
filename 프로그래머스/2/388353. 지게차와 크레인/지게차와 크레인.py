import pprint
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,1,-1]
def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    graph = [['0' for _ in range(m+2)] for __ in range(n+2)]
    for i in range(n):
        for j in range(m):
            graph[1+i][1+j] = storage[i][j]
    
    for req in requests:
        if len(req) == 1:
            # 한글자 삭제 로직
            queue = deque()
            stack = []
            target = req[0]
            queue.append((0,0))
            stack.append((0,0))
            visited = [[False for _ in range(m+2)] for __ in range(n+2)]
            while queue:
                x,y = queue.popleft()
                for i in range(4):
                    new_x = x + dx[i]
                    new_y = y + dy[i]
                    if 0 <= new_x < n+2 and 0 <= new_y< m+2:
                        if graph[new_x][new_y] == '0' and not visited[new_x][new_y]:
                            queue.append((new_x,new_y))
                            visited[new_x][new_y] = True
                        if graph[new_x][new_y] == target:
                            stack.append((new_x,new_y))
                            
                        
            
            
            for x in range(1, n+1):
                for y in range(1, m+1):
                    if graph[x][y] == target:
                        if (x,y) in stack:
                            graph[x][y] = '0'
            for x,y in stack:
                graph[x][y] = '0'
        elif len(req) == 2:
            target = req[0]
            for x in range(1, n+1):
                for y in range(1, m+1):
                    if graph[x][y] == target:
                        graph[x][y] = '0'
    for x in range(1, n+1):
        for y in range(1, m+1):
            if graph[x][y] != '0':
                answer += 1
    
    
    return answer