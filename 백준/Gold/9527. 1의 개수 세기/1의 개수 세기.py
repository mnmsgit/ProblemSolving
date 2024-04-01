import sys

# 2진수로 변환 후 i이하의 자리수의 1의 값 개수의 합은 subset sum 이용

# 2진수로 가장 크게 나올 수 있는 자리 수인 54자리 값 배열 선언


def count(num):
    global dp
    cnt = 0
    bin_num = bin(num)[2:]
    length = len(bin_num)
    for i in range(length):
        if bin_num[i] == '1':
            # num보다 크지 않으면서 가장 큰 2의 거듭제곱 수
            val = length-i-1
            cnt += dp[val]
            # 가장 앞자리 1 개수를 추가로 더해주기
            cnt += (num - 2**val + 1)
            num = num - 2 ** val
    return cnt


x, y = map(int, sys.stdin.readline().split())
dp = [0 for _ in range(55)]

for k in range(1, 55):
    dp[k] = 2**(k-1) + 2 * dp[k-1]

print(count(y) - count(x-1))
