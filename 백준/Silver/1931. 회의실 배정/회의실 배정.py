"""
그리디 알고리즘을 이용한 기초문제
항상 끝나는 시간을 최소로 하는것이 최적의 해를 구하는 방법
"""
import sys

N = int(sys.stdin.readline())
meeting = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    meeting.append([a, b])
meeting.sort()
count = 0
last = 0
for i in range(N):
    if meeting[i][1] < last:
        last = meeting[i][1]
    elif meeting[i][0] >= last:
        last = meeting[i][1]
        count += 1


print(count)
