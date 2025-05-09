from collections import deque
def solution(bridge_length, weight, truck_weights):
    from collections import deque
    waiting = deque(truck_weights)
    tmp = [0] * bridge_length
    bridge = deque(tmp)
    complete = deque()
    weight_on_bridge = 0
    tick = 0
    while len(complete) < len(truck_weights):
        element = 0 # 이번턴에 다리위에 올라갈 트럭 무게
        # 1. 대기 큐에서 제거
        if waiting and weight_on_bridge + waiting[0] -bridge[0] <= weight:
            element = waiting.popleft()
            weight_on_bridge += element
        # 2. 다리위 로직
        out_element = bridge.popleft()
        bridge.append(element)
        # 3. 완료시
        if out_element != 0:
            weight_on_bridge -= out_element
            complete.append(out_element)
        tick +=1
    
    return tick