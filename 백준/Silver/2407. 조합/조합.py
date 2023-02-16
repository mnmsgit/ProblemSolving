import sys

table = [1 for _ in range(101)]

for i in range(1,101):
    table[i] = table[i-1] * i

n, m = map(int, sys.stdin.readline().split())

print(table[n] // table[m] // table[n-m] )
