import sys

# Graph with manually implemented

adj_list = [[1, 7], [0, 2, 7], [1, 3, 6, 7], [2, 4, 6], [3, 5], [4, 6], [2, 3, 5, 7], [0, 1, 2, 6]]

graph = [[0 for _ in range(8)]for _ in range(8)]

D = int(sys.stdin.readline())

# table[n][m] : n -> node, m -> min
table = [[0 for _ in range(D+1)]for _ in range(8)]
table[0][0] = 1

for m in range(1, D+1):
    for n in range(8):
        # n번째 node
        n_node_sum = 0
        for prev_node in adj_list[n]:
            n_node_sum = (n_node_sum + table[prev_node][m-1]) % 1000000007
        table[n][m] = n_node_sum

print(table[0][D])
