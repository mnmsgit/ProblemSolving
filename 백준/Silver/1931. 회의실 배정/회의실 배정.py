import sys

N = int(sys.stdin.readline())
limit = sys.maxsize
cur_end =0
meetings = []
ans = 0
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    meetings.append((a,b))
meetings.sort(key=lambda x: (x[0],x[1]))

for meeting in meetings:
    start = meeting[0]
    end = meeting[1]
    if start >= cur_end:
        ans +=1
        cur_end = end
    else:
        if end <cur_end:
            cur_end = end
print(ans)
