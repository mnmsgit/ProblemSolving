import sys
n, m = map(int, sys.stdin.readline().split())


def f1(a, b):
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i


def f2(a, b):
    for i in range(1, min(a, b)+1):
        num = max(a, b) * i
        if num % min(a, b) == 0:
            return num


print(f1(n, m))
print(f2(n, m))