import sys
input = sys.stdin.readline
N = int(input())
stick_list = []
count = 1

for i in range(1, N+1):
    stick = int(input())
    stick_list.append(stick)
large_stick = stick_list.pop()   # 가장 마지막 스틱을 가장 긴 스틱으로 인식
for i in range(1, N):
    comt_stick = stick_list.pop()
    if comt_stick > large_stick:
        large_stick = comt_stick
        count += 1
print(count)
