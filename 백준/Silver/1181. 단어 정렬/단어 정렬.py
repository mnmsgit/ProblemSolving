import sys

n = int(sys.stdin.readline())
arr = []

for i in range(n):
    arr.append(sys.stdin.readline().strip())
set_lst = set(arr)    # 중복 제거
arr = list(set_lst)
arr.sort()
arr.sort(key=len)

for i in arr:
    print(i)