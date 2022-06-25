K = int(input())

nums = list(map(int, input().split()))
tree = [[]for _ in range(K)]

def maketree(li , depth):
    mid = len(li) // 2
    tree[depth].append(li[mid])
    if len(li) == 1:
        return
    maketree(li[:mid], depth+1)
    maketree(li[mid+1:], depth+1)


maketree(nums, 0)
for i in range(K):
    print(*tree[i])