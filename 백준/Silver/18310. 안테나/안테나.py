# 수학적 사고가 필요한 문제
# 평균값을 이용하여 문제를 풀어야 하는 줄 알았지만 문제에서 사용한 거리는 편차 제곱합(표준편차)가 아니라 편차의 절대값인 절대편차이다.
# 따라서 항상 중앙값이 최소일 수 밖에 없다
# 추가적인 이해를 위해

# 처음 생각한 나의풀이 -> 평균을 구하고 평균값과 가장 가까운 값 출력
# import sys
#
# N = int(sys.stdin.readline())
#
# houses = list(map(int,sys.stdin.readline().split()))
# houses.sort()
# average = sum(houses) / N
# min_distance = average
# ans = houses[0]
# for i in range(N):
#     if abs(average - houses[i]) < min_distance:
#         min_distance = abs(average - houses[i])
#         ans = houses[i]
# print(ans)


# 정답풀이 -> 중간값중 작은 값 출력
import sys

N = int(sys.stdin.readline())

houses = list(map(int,sys.stdin.readline().split()))
houses.sort()
if N % 2:
    print(houses[N // 2])
else:
    print(houses[N//2 -1])
