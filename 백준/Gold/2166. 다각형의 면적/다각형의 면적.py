import sys

N = int(sys.stdin.readline())
points = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    points.append((a, b))
points.append(points[0])

summation = 0

for i in range(N):
    summation += points[i][0] * points[i+1][1]
    summation -= points[i+1][0] * points[i][1]

print(round(abs(summation)/2,2))
