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
        if operators[i]:
            prev_num = num
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
            operators[i] -= 1
            backtracking(num, prev_num, level + 1)
            operators[i] +=1
            num = prev_num


backtracking(A_list[0],0,1)

print(max_ans)
print(min_ans)