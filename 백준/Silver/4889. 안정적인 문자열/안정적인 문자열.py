"""
스택을 이용해 괄호의 정상 여부를 판별하는 문제
후입 선출의 특징을 이용해 닫는 괄호("}") 가 있을때 여는 괄호("{")가 있는 경우만 정상이며 이외의 경우는 모두 안정적이지 못한 상태이다.
괄호가 쌍으로 있으면 안정 상태가 됨을 이용해 계산함.
"""
import sys
from queue import Queue

def find_stable_bracket(alist):
    open_count = 0
    close_count = 0
    for _ in range(len(alist)):
        bracket = alist.pop()
        if bracket == '}':
            close_count += 1
        else:
            if close_count:
                close_count -= 1
            else:
                open_count += 1
    return open_count//2 + open_count % 2 + close_count//2 + close_count % 2


que = Queue()
while True:
    line = sys.stdin.readline().strip()
    brackets = list(line)
    if brackets[0] == "-":
        break
    que.put(find_stable_bracket(brackets))

for i in range(que.qsize()):
    print(f"{i+1}. {que.get()}")

