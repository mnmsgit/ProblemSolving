import sys

def pow(a, b, c):
    if b == 1:
        return a % c
    else:
        x = pow(a, b // 2, c)
        if b % 2 == 1:
            return x ** 2 * a % c
        else:
            return x ** 2 % c

a, b, c = map(int, sys.stdin.readline().split())

print(pow(a, b, c))