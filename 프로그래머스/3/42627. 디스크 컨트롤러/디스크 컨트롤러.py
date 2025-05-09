import heapq

def solution(jobs):
    # 작업 요청 순서 정렬 (요청시간 오름차순)
    jobs.sort()
    
    answer = 0      # 총 대기 시간
    time = 0        # 현재 시간
    i = 0           # jobs에서 꺼낸 작업 수
    hq = []         # 우선순위 큐: (소요시간, 요청시간)

    while i < len(jobs) or hq:
        # 현재 시간까지 들어온 모든 작업을 힙에 넣음
        while i < len(jobs) and jobs[i][0] <= time:
            request, duration = jobs[i]
            heapq.heappush(hq, (duration, request))  # 소요시간 기준으로 정렬
            i += 1

        if hq:
            duration, request = heapq.heappop(hq)
            time += duration
            answer += time - request  # 대기 시간 = 종료 시간 - 요청 시간
        else:
            # 힙에 아무 작업도 없으면 시간만 한 칸 앞으로 이동
            time = jobs[i][0]

    return answer // len(jobs)
