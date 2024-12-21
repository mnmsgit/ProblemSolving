import sys
import copy

N = int(sys.stdin.readline())

points = list(map(int,sys.stdin.readline().split()))
sorted_points = copy.deepcopy(points)
sorted_points = list(set(sorted_points))
sorted_points.sort()
# 좌표 압축 -> 자기 보다 작은 개수가 답

points_with_index = []
points_key = {}
answer = []

for i in range(len(sorted_points)):
    points_key[sorted_points[i]] = i


for element in points:
    answer.append(points_key[element])

print(*answer)
