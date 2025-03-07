# 부르트포스(N^3) 만 피하면 됨

# O(N^2logN) -> 이진탐색 시
# target 설정(두수를 더해서 target 맞추고 싶음)
# left 설정
# right를 이진탐색으로 탐색


# O(N^2) -> 투포인터 이용
# target 설정(두수를 더해서 target 맞추고 싶음)
# 배열에서 투포인터로 N번 만에 확인


import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))

arr.sort()

ans = 0
for i in range(N):
    target = arr[i]
    left = 0
    right = N-1
    while left < right:
        summation = arr[left] + arr[right]
        if summation == target:
            if left == i:
                left +=1
            elif right ==i:
                right -= 1
            else:
                ans += 1
                break
        elif summation < target:
            left += 1
        else:
            right -= 1


print(ans)
