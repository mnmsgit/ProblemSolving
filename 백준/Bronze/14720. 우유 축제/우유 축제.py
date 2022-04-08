import sys
N = int(sys.stdin.readline())
store_list = list(map(int, input().split()))
count = 0
for i in store_list:
    if i == count % 3:
        count += 1
print(count)