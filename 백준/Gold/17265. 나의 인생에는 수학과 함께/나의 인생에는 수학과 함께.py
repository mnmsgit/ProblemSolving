import sys
input = sys.stdin.readline


def operate(operand1,operator,operand2):
    if operator == "*":
        return operand1 * int(operand2)
    if operator == "+":
        return operand1 + int(operand2)
    if operator == "-":
        return operand1 - int(operand2)
    return None


N = int(input())
graph = [[]for i in range(N)]
dp = [[[0,0]for __ in range(N)]for _ in range(N)]
for i in range(N):
    graph[i] = list(input().split())

dp[0][0] = [int(graph[0][0]),int(graph[0][0])]


for x in range(N):
    for y in range(N):
        if (x+y) % 2:
            pass
        else:
            if not x:
                if y:
                    dp[x][y][0] = operate(dp[x][y-2][0], graph[x][y-1], graph[x][y])
                    dp[x][y][1] = operate(dp[x][y-2][1], graph[x][y-1], graph[x][y])
            elif not y:
                dp[x][y][0] = operate(dp[x-2][y][0], graph[x-1][y], graph[x][y])
                dp[x][y][1] = operate(dp[x-2][y][1], graph[x-1][y], graph[x][y])
            else:
                if x > 1 and y > 1:
                    dp[x][y][0] = max(operate(dp[x][y-2][0], graph[x][y-1], graph[x][y]), operate(dp[x-2][y][0], graph[x-1][y], graph[x][y]), operate(dp[x-1][y-1][0],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][0],graph[x][y-1],graph[x][y]))
                    dp[x][y][1] = min(operate(dp[x][y-2][1], graph[x][y-1], graph[x][y]), operate(dp[x-2][y][1], graph[x-1][y], graph[x][y]), operate(dp[x-1][y-1][1],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][1],graph[x][y-1],graph[x][y]))
                if x == 1 and y ==1:
                    dp[x][y][0] = max(operate(dp[x-1][y-1][0],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][0],graph[x][y-1],graph[x][y]))
                    dp[x][y][1] = min(operate(dp[x-1][y-1][1],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][1],graph[x][y-1],graph[x][y]))
                if x == 1 and y != 1:
                    dp[x][y][0] = max(operate(dp[x][y-2][0], graph[x][y-1], graph[x][y]),  operate(dp[x-1][y-1][0],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][0],graph[x][y-1],graph[x][y]))
                    dp[x][y][1] = min(operate(dp[x][y-2][1], graph[x][y-1], graph[x][y]),  operate(dp[x-1][y-1][1],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][1],graph[x][y-1],graph[x][y]))
                if x !=1 and y ==1:
                    dp[x][y][0] = max(operate(dp[x-2][y][0], graph[x-1][y], graph[x][y]), operate(dp[x-1][y-1][0],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][0],graph[x][y-1],graph[x][y]))
                    dp[x][y][1] = min(operate(dp[x-2][y][1], graph[x-1][y], graph[x][y]), operate(dp[x-1][y-1][1],graph[x-1][y],graph[x][y]), operate(dp[x-1][y-1][1],graph[x][y-1],graph[x][y]))


print(*dp[N-1][N-1])

