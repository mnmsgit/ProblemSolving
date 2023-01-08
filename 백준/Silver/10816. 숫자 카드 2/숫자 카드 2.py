# 풀이 1: hashmap(dictionary)이용한 풀이 -> dictionary의 key에 대한 접근은 O(1)의 시간복잡도
# 풀이 2: 이분 탐색을 이용한 풀이 -> O(logN)의 시간복잡도 but 중복된 값 때문에 단순히 찾는 것으로 끝나지 않음
# -> 1. dict 사용(첫 풀이와 비슷) 2. collection의 Counter 사용(list.count는 시간복잡도 높아서 통과 불가)


import sys

N = int(sys.stdin.readline().strip())
N_arr = list(map(int, sys.stdin.readline().split()))
N_dict = {}
M = int(sys.stdin.readline().strip())
M_arr = list(map(int, sys.stdin.readline().split()))
for element in N_arr:
    if element in N_dict:
        N_dict[element] = N_dict[element]+1
    else:
        N_dict[element] = 1

for element in M_arr:
    if element in N_dict:
        print(N_dict[element], end= " ")
    else:
        print(0,end=" ")


#풀이 2


# N_arr.sort()
# for element in M_arr:
#     con = False
#     low = 0
#     high = len(N_arr)-1
#     ele_count =0
#     while low <= high:
#         mid = (low + high)//2
#         if element == N_arr[mid]:
#             con = True
#             break
#         elif element < N_arr[mid]:
#             high = mid-1
#         else:
#             low = mid + 1
#     if con:
#         print(N_dict[element], end=" ")
#     else:
#         print("0", end= " ")
