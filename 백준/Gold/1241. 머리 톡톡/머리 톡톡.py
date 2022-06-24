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