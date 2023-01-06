# top-down으로 생각하면 금방풀 수 있는문제
# dp인줄 알고 풀었으나 메모리 초과로 불가함 -> 쉬운 방범생각
# while 문 사용해도 되지만 무한 루프 문제로 최대 반복횟수를 미리 정해서품
# 이 문제는 bfs로도  풀 수 있다. (queue에 현재원소 *2 , 현재원소 *10 +1) 넣는식 -> bottom-up

import sys

A,B = map(int, sys.stdin.readline().split())
loop_count = len(format(B//A, 'b'))
ans =-1
count =1
for i in range(loop_count):
    if B %2 ==0:
        B //=2
        count += 1
    elif B %10 ==1:
        B //= 10
        count+=1
    if A==B:
        ans = count
        break

print(ans)
