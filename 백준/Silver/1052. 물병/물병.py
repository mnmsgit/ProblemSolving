# 그리디 알고리즘을 이용한 문제
# 난이도가 높지는 않지만 낚시에 걸려 30분, err >= 2**n-1 부호 생각 못해 30분 날린 경험을 주는 문제
# 얻은 점: 1. 문제를 잘 읽자 2. case 나눌때 초기경우, 부호 걸치는 경우 생각 잘하기
# 풀이 1: 2진수 제곱 계산을 이용
# 풀이 2:비트마스킹(비트연산)을 이용하여 풀이 10111010101 => k 가 7인 N이다

# import sys
#
# N, K = map(int, sys.stdin.readline().split())
# err = N - K
# if err <= 0:
#     ans = 0
# else:
#     for i in range(K-1):
#         n = 0
#         while err >= 2**n-1:
#             n += 1
#         if n > 0:
#             err -= 2**(n-1)-1
#     p = 0
#     while err > 2**p-1:
#         p += 1
#     if p >0:
#         err = 2**p-1 - err
#     ans = err
#
# print(ans)


import sys

N, K = map(int, sys.stdin.readline().split())
binaryNum = format(N, 'b')
bin_arr = list(map(int, binaryNum))
if sum(bin_arr) <= K:
    ans = 0
else:
    count = K-1
    for i in range(len(bin_arr)):
        if bin_arr[i] == 1 and count > 0:
            bin_arr[i] = 0
            count -= 1
    bin_arr = map(str,bin_arr)
    bin_result = "".join(bin_arr)
    bin_result = int(bin_result,2)
    a =0
    while bin_result >= 2**a:
        a +=1
    ans = 2**a - bin_result
print(ans)
