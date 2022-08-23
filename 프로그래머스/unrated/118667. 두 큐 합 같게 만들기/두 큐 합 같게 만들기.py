from collections import deque
def solution(queue1, queue2):
    s1 = sum(queue1)
    s2 = sum(queue2)
    n = len(queue1)
    queue1, queue2 = deque(queue1), deque(queue2)
    middle = (s1+s2) // 2 
    answer = 0
    while queue1 and queue2:
        if s1 == middle:
            return answer
        elif s1 > middle:
            a = queue1.popleft()
            s1 -= a
            queue2.append(a)
        else:
            a = queue2.popleft()
            s1 += a
            queue1.append(a)
        answer += 1
        if answer > 3*n:
            return -1
    return -1