n, s = map(int,input().split())
n_list = list(map(int,input().split()))

cnt = 0

def dfs(num,sum):
	global cnt
	if num >= n:
		return
	sum += n_list[num]
	if sum == s:
		cnt += 1


	dfs(num+1,sum)
	dfs(num+1,sum-n_list[num])

dfs(0,0)
print(cnt)