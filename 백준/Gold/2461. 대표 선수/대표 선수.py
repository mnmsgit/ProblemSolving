import sys
import heapq

input = sys.stdin.readline

N, M = map(int,input().split())

students = [[]for _ in range(N)]

min_heap = []
# 각 학급의 현재 진행 index
class_index = [0] * N

max_value = 0
diff = int(1E10)

for i in range(N):
    students[i] = list(map(int,input().split()))
    students[i].sort()
    max_value = max(students[i][0],max_value)
    heapq.heappush(min_heap,(students[i][0],i))


while min_heap:
    now_stat, now_index = heapq.heappop(min_heap)
    now_diff = max_value - now_stat
    diff = min(diff,now_diff)
    if class_index[now_index] ==M-1:
        break
    next_index = class_index[now_index] + 1
    class_index[now_index] = next_index
    next_value = students[now_index][next_index]
    max_value = max(max_value,next_value)
    heapq.heappush(min_heap,(next_value,now_index))

print(diff)


