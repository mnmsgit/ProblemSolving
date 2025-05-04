from collections import deque
def solution(players, m, k):
    debug_mode = False
    
    answer = 0
    # 그리디 알고리즘 접근
    # 서버 큐 (start_time,end_time)
    server_queue = deque()
    
    # 턴마다 진행 로직
    
    # 1. queue에서 가용시간 넘은 서버 제거(복수개 일 수 있음)
    
    # 2. 현재 서버로 진행 가능한지 확인
    # 2.1 안되면 증설 즉, queue에 추가
    
    for turn, player in enumerate(players):
        # 1
        while server_queue and server_queue[0][1] <= turn:
            server_queue.popleft()
        # 2
        while (len(server_queue)+1) * m <= player:
            server_queue.append((turn,turn+k))
            answer +=1
            if debug_mode:
                print(f"turn{turn}에서 서버 추가")
    
    
    return answer