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