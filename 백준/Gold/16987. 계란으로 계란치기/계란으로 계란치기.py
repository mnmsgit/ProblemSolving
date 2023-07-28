def BackTracking(start):

    global ans
    if start==N:
        broken_total=0
        for i in range(N):
            if egg[i][0]<=0:
                broken_total+=1

        ans = max(ans, broken_total)
        return

    if egg[start][0]<=0:
        BackTracking(start+1)
        return

    all_broken_check = True
    for i in range(N):
        if i == start:
            continue
        if egg[i][0]>0:
            all_broken_check = False
            break

    if all_broken_check:
        ans = max(ans , N-1)
        return

    for i in range(N):
        if i == start or egg[i][0]<=0:
            continue
        egg[start][0]-=egg[i][1]
        egg[i][0]-=egg[start][1]
        BackTracking(start+1)
        egg[start][0]+=egg[i][1]
        egg[i][0]+=egg[start][1]


N=int(input())
egg= [list(map(int,input().split())) for _ in range(N) ] #내구도와 무게
ans=0
BackTracking(0)

print(ans)
