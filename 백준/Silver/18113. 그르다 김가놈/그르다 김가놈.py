# 이진 탐색을 이용한 문제
# 주어진 조건은 일반적인 이진탐색(나무자르기)와 다르지 않으나 exceoption 생기는 경우가 존재
# 예외 1. division by zero -> start를 1로 두어 해결
# 예외 2. value error -> max함수의 배열의 크기가 0인 경우 exception 발생

import sys

N, K, M = map(int, sys.stdin.readline().split())
arr = []

for i in range(N):
    kimbap = int(sys.stdin.readline().strip())
    if kimbap >= 2* K:
        kimbap -= 2* K
        arr.append(kimbap)
    elif kimbap >= K:
        kimbap -= K
        arr.append(kimbap)

start = 1
if len(arr) == 0:
    print(-1)
    exit(0)
end = max(arr)
ans = -1

while start <= end:
    mid = (start + end) // 2
    count = 0
    for element in arr:
        count += element // mid
    if count < M:
        end = mid -1
    else:
        ans = mid
        start = mid + 1

print(ans)

