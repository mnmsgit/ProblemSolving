def time_after(time,duration):
    mm = time // 100
    ss = time % 100
    ss += duration
    if ss >=60:
        mm +=1
        ss -=60
    return mm, ss
def solution(schedules, timelogs, startday):
    answer = 0
    members = len(schedules)
    flags = [True] * members
    startday -= 1
    for member_idx in range(members):
        # 출근 시간만 맞으면 됨, startday 5,6 은 주말
        for day in range(7):
            today = day + startday
            today = today % 7
            if today in [5,6]:
                continue
            deadline_mm, deadline_ss = time_after(schedules[member_idx],10)
            arival_mm, arival_ss = timelogs[member_idx][day] // 100,timelogs[member_idx][day] % 100
            if deadline_mm < arival_mm:
                flags[member_idx] = False
            elif deadline_mm == arival_mm:
                if deadline_ss < arival_ss:
                    flags[member_idx] = False 
    
    count = 0
    for flag in flags:
        count +=1
        if flag:
            answer += 1
    
        
    return answer