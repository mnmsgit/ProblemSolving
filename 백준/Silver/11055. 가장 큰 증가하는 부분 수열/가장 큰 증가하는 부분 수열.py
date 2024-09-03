import sys
from copy import deepcopy
input = sys.stdin.readline

N = int(input())

A = list(map(int, sys.stdin.readline().split()))

summation = [0 for _ in range(N)]

summation[0] = A[0]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            summation[i] = max(summation[i],summation[j] + A[i])
        else:
            summation[i] = max(summation[i],A[i])

print(max(summation))