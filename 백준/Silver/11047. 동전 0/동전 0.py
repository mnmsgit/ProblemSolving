# 1원이 항상 있고 큰 동전이 작은 동전의 배수이므로 동전 배열중 가장 큰 값을 선택하는게 local optimal이자 global optimal이다.
# 즉 그리디 알고리즘을 이용하여 쉽게 풀 수 있는 문제이다.
import sys

N, K = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for i in range(N)]
ans = 0

for i in range(N-1, 0, -1):
    if K >= arr[i]:
        ans += K//arr[i]
        K = K % arr[i]
ans += K
print(ans)
