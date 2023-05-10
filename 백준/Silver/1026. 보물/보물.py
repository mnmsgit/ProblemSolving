import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
A.sort()
B.sort(reverse=True)
ans = 0

for i in range(N):
    ans += A[i]*B[i]
print(ans)
# import sys

# N, M = map(int,sys.stdin.readline().split())

# graph = [[] for _ in range(N)]

# for i in range(N):
#     graph[i] = list(map(int, sys.stdin.readline().split()))

# for i in range(M):
#     x1, y1, x2, y2 = map(int,sys.stdin.readline().split())
#     row_iter = x2 -x1
#     col_iter = y2-y1
#     ans =0
#     if col_iter:
#         for j in range(x1-1, x2-1):
#             if not row_iter:
#                 for k in range(y2-1,y1-1):
#                     ans += graph[j][k]
#             else:
#                 ans += graph[j][y2-1]
#     else:
#         if row_iter:
#             for k in range(y2-1,y1-1):
#                 ans += graph[x1-1][k]
#         else:
#             ans += graph[x1-1][y1-1]
#     print(ans)
