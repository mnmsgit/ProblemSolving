import sys
n = int(sys.stdin.readline())
z_tree = [[]for _ in range(n)]
visited = [[-1 for _ in range(n)]for i in range(n)]

for i in range(n):
    z_tree[i] = list(map(int, sys.stdin.readline().split()))


def left_num(depth, index):
    return z_tree[depth+1][index]


def right_num(depth, index):
    return z_tree[depth+1][index+1]


def traversal(depth, index):
    if depth == n-2:
        visited[depth][index] = z_tree[depth][index] + max(left_num(depth, index), right_num(depth,index))
        return visited[depth][index]
    if visited[depth+1][index] != -1 and visited[depth+1][index+1] != -1:
        visited[depth][index] = z_tree[depth][index] + max(visited[depth+1][index], visited[depth+1][index+1])
    else:
        visited[depth][index] = z_tree[depth][index] + max(traversal(depth+1, index), traversal(depth+1, index+1))
    return visited[depth][index]


if n==1:
    print(z_tree[0][0])
else:
    print(traversal(0, 0))
