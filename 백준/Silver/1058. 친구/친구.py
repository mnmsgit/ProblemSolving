# n의 개수가 작기 때문에 전체 탐색(프루트 포스)로 해결할 수 있는 문제
# 이중 for 문으로도 n<=50 이므로 O(n**2)가 가능하기 때문에 graph 전체를 탐색 

import sys
N = int(sys.stdin.readline())


fr_list = [[0] * N for i in range(N)]
list2 = [[0] * N for i in range(N)]
for i in range(N):
    a = input()
    fr_list[i] = list(a)


def find_max_friend():
    a = []
    for i in range(N):
        count = 0
        for j in range(N):
            if fr_list[i][j] == 'Y':
                list2[i][j] = 1
                for k in range(N):
                    if fr_list[j][k] == 'Y' and i != k:
                        list2[i][k] = 1
        for j in range(N):
            if list2[i][j] == 1:
                count += 1
        a.append(count)

    return max(a)


print(find_max_friend())
