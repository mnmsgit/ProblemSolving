from collections import deque
def solution(players, m, k):
    answer = 0
    # 19:50
    # 그리디
    
    server_count = 0
    queue = deque()
    
    tick = 0
    for player in players:
        # 서버 반납
        while queue:
            if queue[0] <= tick:
                queue.popleft()
            else:
                break
        # 서버 증설
        while True:
            needed_server = player//m 
            now_server_count = len(queue)
            if now_server_count < needed_server:
                queue.append(tick+k)
                print(f"서버추가 턴 {tick}")
                answer +=1
            else:
                break
                
        tick +=1
    return answer