import sys


def avg(arr):
    a = 0
    for element in arr:
        a += element
    return int(round(a/len(arr)))


def middle(arr):
    return arr[(len(arr)//2)]


def ran(arr):
    if len(arr) > 1:
        return arr[-1] - arr[0]
    else:
        return 0


def freq(arr):
    fre = []
    max_counts = 1
    counts = 0
    for i in range(len(arr)):
        if i:
            if arr[i] == arr[i-1]:
                counts += 1
                if counts > max_counts:
                    max_counts = counts
                    fre.clear()
                    fre.append(arr[i])
                elif counts == max_counts:
                    fre.append(arr[i])
            else:
                counts = 0
    if not fre:
        if len(arr) < 2:
            return arr[0]
        else:
            return arr[1]
    else:
        if len(fre) < 2:
            return fre[0]
        else:
            return fre[1]


n = int(sys.stdin.readline().strip())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    nums.append(num)
nums.sort()
print(avg(nums))
print(middle(nums))
print(freq(nums))
print(ran(nums))
