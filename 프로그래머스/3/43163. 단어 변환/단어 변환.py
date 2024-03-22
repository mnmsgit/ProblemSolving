from collections import deque
def issimilar(w1,w2):
    length = len(w1)
    cnt = 0
    for i in range(length):
        if w1[i] == w2[i]:
            cnt +=1
    if cnt == length-1:
        return True
    return False
    
    
def solution(begin, target, words):
    word_length = len(begin)
    graph = [[] for _ in range(len(words))]
    words_order = {}
    # 그래프 생성
    for i in range(len(words)):
        words_order[words[i]] = i
        for j in range(i+1,len(words)):
            if issimilar(words[i],words[j]):
                graph[i].append(j)
                graph[j].append(i)
                
    print(words_order)
    # BFS
#     ### visited = [False for _ in range(word_length)]
    step = [0 for _ in range(len(words))]
    
    if target not in words_order:
        print("no key")
        return 0
    
    target_idx = words_order[target]
    
    queue = deque()
    for i in range(len(words)):
        if issimilar(words[i],begin):
            queue.append(i)
            step[i] = 1
            
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if step[next_node] == 0:
                step[next_node] = step[node] +1
                queue.append(next_node)
    answer = step[target_idx]
    # print(step)
    # if answer == -1:
    #     answer = 0
    return answer