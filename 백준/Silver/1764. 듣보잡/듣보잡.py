import sys

N, M = map(int, sys.stdin.readline().split())

a = set()
ans = []
for i in range(N):
    a.add(sys.stdin.readline().strip())
for k in range(M):
    voca = sys.stdin.readline().strip()
    if voca in a:
        ans.append(voca)
print(len(ans))
ans.sort()
for o in range(len(ans)):
    print(ans[o])
    
