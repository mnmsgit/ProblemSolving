import sys
ans =[]
for i in range(10):
    a = int(sys.stdin.readline()) % 42
    if a not in ans:
        ans.append(a)
print(len(ans))