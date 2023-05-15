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
