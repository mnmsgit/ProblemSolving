import sys
line = sys.stdin.readline().rstrip().split("-")
a = 0
b = 0
for i in range(len(line)):
    if not i:
        for nums in list(map(int, line[i].split("+"))):
            a += nums
    else:
        for element in list(map(int, line[i].split("+"))):
            b += element
print(a-b)
