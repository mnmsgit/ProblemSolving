import sys


N = sys.stdin.readline()
arr = list(map(int,sys.stdin.readline().split()))
M = sys.stdin.readline()
nums_list = list(map(int,sys.stdin.readline().split()))

num_set = set(arr)

for num in nums_list:
	if num in num_set:
		print(1)
	else:
		print(0)
	
	