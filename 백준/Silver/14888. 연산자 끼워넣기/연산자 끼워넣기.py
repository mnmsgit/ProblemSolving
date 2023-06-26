# backtrecking 활용 기본 예시
# 연산자는 N-1개 주어질 것 이므로 전체 가능한 최대 경우가 10! 개 정도로 적음 -> backtracking 사용
# backtracking 할 때 연산 하기 전 수 (전 level의 인자) 가 필요하다고 느껴 prev_num 추가
import sys

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
operators = list(map(int, sys.stdin.readline().split()))
min_ans = sys.maxsize
max_ans = -sys.maxsize


def backtracking(num, prev_num, level):
    global max_ans
    global min_ans
    if level == N:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans,num)
        return
    for i in range(4):
        if operators[i]: # operator를 앞에서 부터 사용하여 없는 경우 다음 index의 operator 사용
            prev_num = num # backtrack 되었을 때를 위한 두 번째 인자 값
            if i == 0:
                num += A_list[level]
            elif i == 1:
                num -= A_list[level]
            elif i == 2:
                num *= A_list[level]
            elif i == 3:
                if num < 0:
                    num = -((-num)//A_list[level])
                else:
                    num //= A_list[level]
            # operator 수 줄이고 (사용 했기 때문)
            operators[i] -= 1
            # 다음 level로의 재귀 탐색
            backtracking(num, prev_num, level + 1)
            # backtracking 되었을 때 위의 연산의 있기 전의 상태로 돌려 주는 로직
            operators[i] +=1
            num = prev_num


backtracking(A_list[0],0,1)

print(max_ans)
print(min_ans)
