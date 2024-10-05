import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
	N, K = map(int,input().split())
	graph = []
	ans = [[0 for __ in range(N-K+1)] for _ in range(N-K+1)]
	for i in range(N):
		graph.append(list(map(int,input().split())))
	
	# 초기 세팅
	for row in range(K):
		for col in range(K):
			ans[0][0] += graph[row][col]
	trash =ans[0][0]
	for col_start in range(N-K):
		tmp = ans[0][col_start]
		for i in range(K):
			tmp += graph[i][col_start+K]
			tmp -= graph[i][col_start]
		ans[0][col_start+1] = tmp
		trash = min(trash, tmp)
		
	for row_start in range(N-K):
		for col_start in range(N-K+1):
			tmp = ans[row_start][col_start]
			tmp += sum(graph[row_start+K][col_start:col_start+K]) 
			tmp -= sum(graph[row_start][col_start:col_start+K])
			ans[row_start+1][col_start] = tmp
			trash = min(trash, tmp)
	# trash = min(min(ans))
	print(trash)
