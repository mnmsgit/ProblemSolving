import sys

MAX_SIZE = 1000000
prime = [1] * (MAX_SIZE+1)
prime[0] = 0
prime[1] = 0

for i in range(2 , MAX_SIZE+1):
    multiplicand = 2 * i
    while multiplicand <= MAX_SIZE:
        prime[multiplicand] = 0
        multiplicand += i

N, M = map(int, sys.stdin.readline().split())

for i in range(N,M+1):
    if i * prime[i]:
        print(i)
