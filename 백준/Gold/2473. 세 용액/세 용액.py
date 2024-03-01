import sys
from itertools import combinations
N = int(sys.stdin.readline())

solution = list(map(int, sys.stdin.readline().split()))
solution.sort()

left = 0
right = N - 1
ans = [solution[left], solution[left+1], solution[right]]

for fix in range(N):
    left = fix + 1
    right = N-1
    while left < right:
        stir = solution[left] + solution[right] + solution[fix]
        if abs(sum(ans)) > abs(stir):
            ans = [solution[left], solution[fix], solution[right]]
        if stir < 0:
            left +=1
        elif stir >0:
            right -=1
        else:
            break
ans.sort()
print(*ans)

