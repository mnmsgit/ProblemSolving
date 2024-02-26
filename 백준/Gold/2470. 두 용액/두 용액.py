import sys

N = int(sys.stdin.readline())
solution = list(map(int,sys.stdin.readline().split()))
solution.sort()
low = 0
high = N-1
ans = [solution[low], solution[high]]
while low < high:
    stir = solution[low] + solution[high]
    if abs(stir) < abs(sum(ans)):
        ans = [solution[low], solution[high]]
    if stir < 0:
        low += 1
    else:
        high -= 1

print(*ans)
