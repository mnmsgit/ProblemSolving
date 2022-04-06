def division(a, b):
    min_a = a-b*(b+1)/2
    if min_a < 0:
        return -1
    elif min_a % b == 0:
        return k-1
    else:
        return k
n,k = input().split()
n = int(n)
k = int(k)
print(division(n, k))
