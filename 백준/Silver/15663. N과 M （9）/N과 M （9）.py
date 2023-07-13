import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
visited = [False] * N


temp_ans = set()


def backtracking(ans):
    if len(ans) == M:
        temp_ans.add(tuple(ans))
        return
    for i in range(N):
        if len(ans) == 0 or not visited[i]:
            ans.append(arr[i])
            visited[i] = True
            backtracking(ans)
            visited[i] = False
            ans.pop()


backtracking([])

sorted_ans = list(temp_ans)
sorted_ans.sort()
for element in sorted_ans:
    print(*element)