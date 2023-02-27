# 스택 알면 풀 수 있는 기초 문제
import sys

K = int(sys.stdin.readline())

stack = []
for i in range(K):
    money = int(sys.stdin.readline())
    if not money:
        stack.pop()
    else:
        stack.append(money)

print(sum(stack))
