from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque(truck_weights)
    tick =0
    bridge = deque()
    
    while True:
        # 다리 감소
        for i in range(len(bridge)):
            bridge[i][0] -=1
        # 나갈애 보내기
        if bridge and bridge[0][0]==0:
            bridge.popleft()
        # 시간 올리기
        tick +=1
        # 다리 올리기
        sum_weight = 0
        for i in range(len(bridge)):
            sum_weight += bridge[i][1]
        if queue and sum_weight + queue[0] <= weight:
            bridge.append([bridge_length,queue[0]])
            queue.popleft()
        # 종료 조건 -> 
        if not queue and not bridge:
            break
    return tick