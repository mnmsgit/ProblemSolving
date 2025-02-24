# set(슬라이싱한 이후 ) X 2중 loop -> N^^3의 시간복잡도 -> 시간초과
# 슬라이딩 윈도우 사용 -> 시간초과 N^2가 안됨
# 투 포인터 사용
import sys

N = int(sys.stdin.readline())

S = list(map(int, sys.stdin.readline().split()))

max_length = -1
fruit_count = [0] * 10
left = 0


def fruit_set(arr):
    count = 0
    for f in arr:
        if f:
            count += 1
    return count


# 오른쪽 결정
for right in range(N):
    fruit_count[S[right]] += 1
    while fruit_set(fruit_count) > 2:
        # 2개 이상일시 left을 증가(greedy)
        fruit_count[S[left]] -= 1
        left += 1
    max_length = max(max_length, right - left + 1)

print(max_length)
