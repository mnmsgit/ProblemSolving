import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A_sort = [[0]for _ in range(N+1)]
    # B_sort = [[0]for _ in range(N+1)]
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        A_sort[a] = b
        # B_sort[b] = a
    min_b = 0
    passer = 0
    for i in range(1, N+1):
        if i == 1:
            min_b = A_sort[i]
        if A_sort[i] <= min_b:
            passer += 1
            min_b = A_sort[i]
    print(passer)