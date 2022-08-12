import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    A_sort = [[0]for _ in range(N+1)]
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        A_sort[a] = b
    max_b = A_sort[1]  # 지원자의 b등수가 max_b보다 낮아야 채용가능
    passer = 0
    for i in range(1, N+1):
        b_rank = A_sort[i]
        if b_rank <= max_b:
            passer += 1
            max_b = b_rank
            if b_rank == 1:
                break
    print(passer)
