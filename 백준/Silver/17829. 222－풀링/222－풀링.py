import sys

N = int(sys.stdin.readline())
graph = [[]for _ in range(N)]
divide = []
for i in range(N):
    graph[i] = list(map(int,sys.stdin.readline().split()))

# def find_max_2(arr):
#     ans =[]
#     ans = arr
#     ans.sort()
#     return ans[3]

dx = [0,0,1,1]
dy = [0,1,0,1]


def d_c(size):
    loop_count = size // 2
    new_graph = [[0 for _ in range(loop_count)]for __ in range(loop_count)]
    for k in range(loop_count):
        for j in range(loop_count):
            ans = []
            for z in range(4):
                ans.append(graph[k*2+dx[z]][j*2+dy[z]])
            ans.sort()
            new_graph[k][j] = ans[2]
    return new_graph


si = N
while si != 2:
    graph = d_c(si)
    si //= 2

print(d_c(si)[0][0])