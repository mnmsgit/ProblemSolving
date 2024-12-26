"""
segment tree(index tree, Fenwick tree) 개념 문제

아래의 내용이 필요
1. index tree의 구조 이해(LSB의 대한 이해)
2. tree update
3. 누적합

N 개 원소에 대해 누적 합과 update를 O(log N)으로 보장

"""
import sys

n, m, k = map(int,sys.stdin.readline().split())

nums = [0] * (n+1)
tree = [0] * (n+1)


# 누적합 계산
def prefix_sum(x: int) -> int:

    result = 0
    while x > 0:
        result += tree[x]
        # LSB만큼 빼면서 진행
        x -= (x & -x)
    return result


# update 함수 -> x번째 index를 amount만큼 추가
def update(x: int, amount: int) -> None:
    global tree
    # x==n 경계 주의! n이 2의 제곱수일 경우 문제
    while x <= n:
        tree[x] += amount
        # n보다 작은 2의 제곱수까지 수까지 진행
        x += (x & -x)


for i in range(1,n+1):
    num = int(sys.stdin.readline())
    nums[i] = num
    update(i, num)

for _ in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        # update b번째 값을 c로
        update(b, c-nums[b])
        nums[b] = c
    else:
        # 구간 합  -> c 까지의 누적 합 - (b-1)까지 누적 합
        ans = prefix_sum(c) - prefix_sum(b-1)
        print(ans)


