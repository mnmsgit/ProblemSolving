# import sys
# import math
#
# '''
# case1: 같은 행에서 생기는 등차수열
# case2: 같은 열에서 생기는 등차수열
# case3: 다른 행과 다른 열에서 생기는 등차수열(대각선)
#
# '''
#
#
# def find_square_num(n):  # 제곱수면 true를 아니면 false를 반환하는 함수
#     if math.sqrt(n) % 1 == 0.0:
#         return True
#     else:
#         return False
#
#
# def find_sequence_in_col(rows, cols, len_digits):  # case1
#     new_list = []
#     max_d = math.floor((cols - 1) / (len_digits - 1))  # 등차수열의 공차의 최대값
#     for row in range(rows):
#         for d in range(1, max_d + 1):  # 공차 d 값에 따라 반복 (d값을 고정)
#             max_a1 = cols - (len_digits - 1) * d
#             for a1 in range(max_a1):  # 첫째항 a_1 값에 따라 반복
#                 temp_list = []
#                 for digit in range(1, len_digits + 1):  # 몇번째 항인지에따라 반복
#                     temp_list.append(a_list[row][a1 + ((digit - 1) * d)])
#                 new_list.append(''.join(map(str, temp_list)))
#                 temp_list.reverse()
#                 new_list.append(''.join(map(str, temp_list)))
#     return new_list
#
#
# def find_sequence_in_row(rows, cols, len_digits):  # case2
#     new_list = []
#     max_d = math.floor((rows - 1) / (len_digits - 1))
#     for col in range(cols):
#         for d in range(1, max_d + 1):
#             max_a1 = rows - (len_digits - 1) * d
#             for a1 in range(max_a1):
#                 temp_list = []
#                 for digit in range(1, len_digits + 1):  # 몇번째 항인지에따라 반복
#                     temp_list.append(a_list[a1 + ((digit - 1) * d)][col])
#                 new_list.append(''.join(map(str, temp_list)))
#                 temp_list.reverse()
#                 new_list.append(''.join(map(str, temp_list)))
#     return new_list
#
#
# def find_sequence_in_rows_and_cols(rows, cols, len_digits):
#     new_list = []
#     max_col_d = math.floor((cols - 1) / (len_digits - 1))
#     max_row_d = math.floor((rows - 1) / (len_digits - 1))
#     for row_d in range(1, max_row_d + 1):
#         max_row_a1 = rows - (len_digits - 1) * row_d
#         for col_d in range(1, max_row_d + 1):
#             max_col_a1 = cols - (len_digits - 1) * col_d
#             for row_a1 in range(max_row_a1):
#                 for col_a1 in range(max_col_a1):
#                     temp_list = []
#                     for digit in range(1, len_digits + 1):  # 몇번째 항인지에따라 반복
#                         temp_list.append(a_list[row_a1 + ((digit - 1) * row_d)][col_a1 + ((digit - 1) * col_d)])
#                     new_list.append(''.join(map(str, temp_list)))
#                     temp_list.reverse()
#                     new_list.append(''.join(map(str, temp_list)))
#                     temp_list = []
#                     for digit in range(1, len_digits + 1):  # 몇번째 항인지에따라 반복
#                         temp_list.append(
#                             a_list[rows - row_a1 - 1 - ((digit - 1) * row_d)][col_a1 + ((digit - 1) * col_d)])
#                     new_list.append(''.join(map(str, temp_list)))
#                     temp_list.reverse()
#                     new_list.append(''.join(map(str, temp_list)))
#     return new_list
#
#
# N, M = map(int, input().split())
# a_list = []
#
# for _ in range(N):
#     a_list.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))
# digits = max(N, M)  #digit은 자릿수의 최댓값 완전제곱수가 없는경우 max_digit을 1자리씩 줄이며 찾아갈 것임
#
# looping = True
#
# while looping:
#     possible_lists = []
#     if digits == 1:  # 한자리 숫자가 완전제곱수
#         for n in range(N):
#             for c in range(M):
#                 possible_lists.append(a_list[n][c])
#         possible_lists.sort(reverse=True)
#         for possible_list in possible_lists:
#             if find_square_num(possible_list):
#                 print(possible_list)
#                 looping = False
#                 break
#     elif digits == 0:
#         print(-1)
#         break
#     else:
#         if min(N, M) < digits:  # 자리수가  M,N의 최솟값보다 큰 경우 case 1 과 case 2 하나만 가능
#             if N < M:  # col(열)이 더 큰경우 같은행에서 공차수열이 존재
#                 possible_lists.extend(find_sequence_in_col(N, M, digits))
#             else:
#                 possible_lists.extend(find_sequence_in_row(N, M, digits))
#         else:  # 자리수가 행과 열의 최솟값보다 작거나 같은 경우 모든 case가능
#             possible_lists.extend(find_sequence_in_col(N, M, digits))
#             possible_lists.extend(find_sequence_in_row(N, M, digits))
#             possible_lists.extend(find_sequence_in_rows_and_cols(N, M, digits))
#         possible_lists = list(map(int, possible_lists))
#         possible_lists.sort(reverse=True)
#         for possible_list in possible_lists:
#             if find_square_num(possible_list):
#                 print(possible_list)
#                 looping = False
#                 break
#
#     digits -= 1
import sys
import math

M, N = map(int, sys.stdin.readline().split())

numbers = []
for _ in range(M):
    numbers.append(list(map(int, list(sys.stdin.readline().replace('\n', '')))))

result = -1

for m in range(M):  # 어느 행에서 시작할 것인가?
    for n in range(N):  # 어느 열에서 시작할 것인가?
        for weight_m in range(-M, M):  # 행에서의 공차. -M부터 시작
            for weight_n in range(-N, N):  # 열에서의 공차. -N부터 시작
                # 두 공차가 모두 0이면 무한 루프
                if weight_m == 0 and weight_n == 0: continue
                step = 0
                x = m
                y = n
                value = ''
                # 입력받은 수들의 범위 안에서 가능한 수열 추출
                while (0 <= x < M) and (0 <= y < N):
                    # 숫자 조합을 하고
                    value += str(numbers[x][y])
                    step += 1

                    # 제곱수이고, 최댓값 갱신이 가능한지 확인
                    value_int = int(''.join(value))
                    value_sqrt = math.sqrt(value_int)
                    value_decimal = value_sqrt - int(value_sqrt)
                    if value_decimal == 0 and value_int > result: result = value_int

                    x = m + step * weight_m
                    y = n + step * weight_n

print(result)