# N은 점 K는 구간
# 위치를 정렬하고 인접한 거리를 저장
# 거리가 항상 작은 것을 선택, 만약 모든 거리를 선택하거나 센서 -기지국 수 만큼 반복이 완료되면 종료
# 기지국이 더 같거나 많은경우 구간이 생기지 않으므로 0
import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
location = list(map(int,sys.stdin.readline().split()))
location.sort()
sensor_distance = []
for i in range(1, N):
    sensor_distance.append(location[i] - location[i-1])
sensor_distance.sort(reverse= True)

ans = 0
if N > K:
    count = N-K
    while sensor_distance and count:
        ans += sensor_distance.pop()
        count -= 1
print(ans)
