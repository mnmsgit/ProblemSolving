from collections import deque
def bfs(x,y,visited,maps):
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    queue = deque()
    queue.append((x,y))
    island = int(maps[x][y]) 
    visited[x][y] = True
    while queue:
        node_x, node_y = queue.popleft()
        for i in range(4):
            new_x = node_x + dx[i]
            new_y = node_y + dy[i]
            if -1<new_x<len(maps) and -1<new_y<len(maps[0]):
                if not visited[new_x][new_y] and maps[new_x][new_y] != 'X':
                    queue.append((new_x,new_y))
                    island += int(maps[new_x][new_y])
                    
                    visited[new_x][new_y] = True
    return island
        
    
    
def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for __ in range(len(maps))]
    for x in range(len(maps)):
        for y in range(len(maps[0])):
            if maps[x][y] !="X" and not visited[x][y]:
                answer.append(bfs(x,y,visited,maps))
                
    if not answer:
        answer = [-1]
    answer.sort()
    return answer