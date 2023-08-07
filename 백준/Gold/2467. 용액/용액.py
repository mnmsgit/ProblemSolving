import sys
N = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
arr.sort()
p1 = 0
p2 = N-1
ans_left = arr[0]
ans_right = arr[-1]
ans = abs(arr[p1]+arr[p2])
while p1 < p2:
    temp_sub = arr[p1]+arr[p2]
    if abs(temp_sub) <= ans:
        ans_left = arr[p1]
        ans_right = arr[p2]
        ans = abs(temp_sub)
    if temp_sub < 0:
        p1 += 1
    if temp_sub > 0:
        p2 -= 1
    if not temp_sub:
        break

print(ans_left,ans_right)
