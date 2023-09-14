import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
x = int(sys.stdin.readline())

arr.sort()
low =0
high = n-1
ans =0
while low < high:
    if arr[low]+arr[high] == x:
        ans += 1
        low += 1
        high -= 1
    elif arr[low]+arr[high] >x:
        high -=1
    else:
        low +=1
print(ans)

