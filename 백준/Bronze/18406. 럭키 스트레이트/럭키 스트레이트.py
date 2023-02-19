import sys

N = sys.stdin.readline().strip()
length = len(N)
ans = "READY"
combo = 0
for i in range(length//2):
    combo += int(N[i])
    combo -= int(N[length//2+i])
if not combo:
    ans = "LUCKY"
print(ans)

