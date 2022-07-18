"""
큐의 성질을 변형한 문제
처음 문제를 보았을 때는 우선순위큐(priority queue)를 이용한 문제 처럼 보였으나 같은 우선순위에서 선입선출이 아닌 특수한 조건이 있기 때문에 단순 큐(리스트)를 이용한 풀이
내림차순으로 sort된 배열을 이용해 남아있는 수 중 가장 큰수를 구하는데 이용 -> 기본내장함수 max를 이용해도 될 것 같다.
"""
import sys
n = int(sys.stdin.readline())
for _ in range(n):
    m, index = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))
    priority_sort = sorted(priority, reverse=True)
    count = 0
    while priority:
        a = priority.pop(0)
        if a == priority_sort[0]:
            count += 1
            priority_sort.pop(0)
            if not index:
                print(count)
                break
        else:
            priority.append(a)
            if not index:
                index += len(priority)
        index -= 1
