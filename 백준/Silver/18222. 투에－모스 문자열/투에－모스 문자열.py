import sys
K = int(sys.stdin.readline())
print(format(K-1, 'b').count('1') % 2)
