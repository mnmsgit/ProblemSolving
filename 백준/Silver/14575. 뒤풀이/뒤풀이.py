import sys

N, T = map(int,sys.stdin.readline().split())
L = []
R = []
range_set = []
for i in range(N):
    l, r = map(int, sys.stdin.readline().split())
    L.append(l)
    R.append(r)
    range_set.append([l, r])

if sum(L) > T or sum(R) < T:
    print(-1)
    exit(0)

low = max(L)
high = max(R)

ans = high
while low < high:
    mid = (low + high) // 2
    temp = 0
    for element in range_set:
        if mid > element[1]:
            temp += element[1]
        else:
            temp += mid

    if temp >= T:
        ans = mid
        high = mid
    else:
        low = mid+1

print(ans)
