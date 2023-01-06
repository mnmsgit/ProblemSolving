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
