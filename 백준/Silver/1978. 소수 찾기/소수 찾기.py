import sys

N = int(sys.stdin.readline())

table = [2]
for i in range(2,1001):
    con = True
    for element in table:
        if not i % element:
            con = False
    if con:
        table.append(i)
ans = 0
arr = list(map(int,sys.stdin.readline().split()))
for element in arr:
    if element in table:
        ans +=1
print(ans)
