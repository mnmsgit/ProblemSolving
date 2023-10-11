import sys

N = int(sys.stdin.readline())
limits = list(map(int, sys.stdin.readline().split()))
limits.sort(reverse=True)
M = int(sys.stdin.readline())
boxs = list(map(int, sys.stdin.readline().split()))
boxs.sort(reverse=True)

if boxs[0] > limits[0]:
    print(-1)
    # 종료조건 추가
    exit(0)

time = 0
while boxs:
    if not boxs:
        break
    for limit in limits:
        for box in boxs:
            if limit >= box:
                boxs.remove(box)
                break
    time += 1
print(time)
