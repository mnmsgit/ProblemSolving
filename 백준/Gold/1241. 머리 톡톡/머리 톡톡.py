"""
각각의 학생이 머리를 "톡톡"하는 경우는 자신의 상대방의 배수일 때 이다.
n으로 받을 수 있는 가장 큰 숫자 인 1000000 을 크기로 한 배열을 만들고 학생의 숫자가 아닌 배열에는 0 학생의 숫자가 맞는배열에는 +1씩 더한다.
소인수 분해는 루트 기준으로 더 작은 숫자들만 계산해도 되기 때문에 이를 이용해 시간복잡도를 줄인다.
"""
import sys
import math

N = int(sys.stdin.readline())
table = []
num_li = [0 for _ in range(1000001)]
for _ in range(N):
    num = int(sys.stdin.readline())
    table.append(num)
    num_li[num] += 1
for num in table:
    result = 0
    temp_li = []
    middle_num = int(math.sqrt(num))
    for n in range(1, middle_num + 1):
        if num % n == 0:
            if n ** 2 == num:
                result += num_li[n]
            else:
                result += num_li[n]
                result += num_li[num // n]
    print(result - 1)
