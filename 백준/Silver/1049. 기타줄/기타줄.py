# 그리디 알고리즘을 이용한 기본 문제
# 1. 6개 가격을 모아둔 배열, 1개가격을 모아둔 배열을 각각 오름차순 정렬 -> 최솟값을 구하고 수량이 무제한이기 때문에 각 배열의 최솟값만 사용
# 2. 6개 가격의 최소값이 1개가격의 6배보다 크면 1개가격만 이용하여 전체 구입
# 3. 아닌 경우 줄의 개수 n을 6으로 나눈 몫 만큼 6개로 사고 6개짜리를 하나 더살지 낮개로 나머지(0~5)개를 살지 결정

import sys

N, M = map(int, sys.stdin.readline().split())

arr1 = []
arr2 = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr1.append(a)
    arr2.append(b)

arr1.sort()
arr2.sort()
ans =0
if arr1[0] >= arr2[0]* 6:
    ans = arr2[0] * N
else:
    ans = arr1[0] * (N//6)
    ans += min(arr1[0], arr2[0] * (N % 6))
print(ans)
