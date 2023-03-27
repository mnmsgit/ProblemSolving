# 이진탐색의 대표 문제
# 가능한 M(나무 길이)의 범위가 1이상 2,000,000,000 이하이고 N(나무의 수)의 범위는 1이상 1,000,000이하이다.
# 이때 N*M번의 반복으로는 10조 가량의 연산량이 필요하므로 시간초과가 난다.
# 따라서 나무의 높이를 정활때 최소값: 0 최대값: 나무중 가장 높은 나무로 두고 이진탐색을 통해 높이M을 결정 하여 최대 연산을 log(2,000,000,000) * 1,000,000로 둘 수 있다.
# p.s 이 문제는 파이썬으로 풀 경우 if/else문의 위치만 바꿔도 시간초과가 난다. + 반복문이 많은 경우 pypy3 에서는 시간이 상대적으로 여유롭게 통과가 된다.
# 2주차 dp문제
import sys

N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

result = 0
while low <= high:
    mid = (low + high)//2
    cut = 0
    for tree in trees:
        if tree > mid:
            cut += tree - mid
    if cut < M:
        high = mid - 1
    else:
        result = mid
        low = mid + 1
print(result)

