# 그리디 알고리즘을 사용한 문제
# 구현은 매우 쉬우나 개념을 생각하기에 오래 걸린 문제
# 가설 : 키차이를 가장 적게 하고 싶으므로 키차이를 미리 구해둔다.
# a,b,c 순서일 때 키 차이는 c-a= (c-b) + (b-a)와 같다.
# 따라서 greedy하게 키차이가 적은 원소를 선택 하면 결과는 키 차이가 많이 나는 k개를 제외하게 된다.


import sys

N, K = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))
diff = []

for i in range(N-1):
    diff.append(arr[i+1]-arr[i])

diff.sort(reverse=True)
diff = diff[K-1:]
ans = sum(diff)
print(ans)
