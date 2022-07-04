import sys


def sorting(a):
    n = len(a)
    if n < 2:
        return a
    mid = n // 2
    g1 = sorting(a[:mid])
    g2 = sorting(a[mid:])
    result = []
    while g1 and g2:
        if g1[0] <= g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    if g1:
        result.extend(g1)
    if g2:
        result.extend(g2)
    return result


def find_fake(li):
    for i in range(9):
        fi = heights[i]
        for j in range(i + 1, 9):
            se = heights[j]
            if sum_he == fi + se:
                heights.pop(j)
                heights.pop(i)
                return


heights = []
sum_he = 0
for _ in range(9):
    height = int(sys.stdin.readline().strip())
    heights.append(height)
    sum_he += height
sum_he -= 100
heights = sorting(heights)
find_fake(heights)

for element in heights:
    print(element)
