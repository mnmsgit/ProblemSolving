def fill_snail(graph, start, size, idx):
    if size ==0:
        return
    if size == 1:
        graph[start[0]][start[1]] = idx
        return
    for i in range(size-1):
        graph[start[0]+i][start[1]] = idx
        idx +=1
    for i in range(size-1):
        graph[start[0]+size-1][start[1]+i] = idx
        idx +=1
    for i in range(size-1):
        graph[start[0]+size-1-i][start[1]+size-1-i] = idx
        idx +=1
    if size > 3:
        new_start = (start[0]+2,start[1]+1)
        new_size = size - 3
        fill_snail(graph,new_start,new_size,idx)
        

def solution(n):
    answer = []
    graph =  [[-1 for i in range(j+1)]for j in range(n)]
    fill_snail(graph, (0,0),n, 1)
    for i in range(n):
        answer.extend(graph[i])
    return answer