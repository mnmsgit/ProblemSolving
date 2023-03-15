import sys

L, R = map(int, sys.stdin.readline().split())

count = 0

str_L = str(L)
str_R = str(R)

if len(str_R) - len(str_L) > 0:
    count = 0
else:
    for i in range(len(str_R)):
        if str_R[i] == str_L[i]:
            if str_R[i] == '8':
                count +=1
        else:
            break

print(count)
