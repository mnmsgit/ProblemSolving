import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())

table = [[] for _ in range(N)]

members = [ i for i in range(N)]
ans = int(10E10)

for i in range(N):
    table[i] = list(map(int,sys.stdin.readline().split()))

for member_list in combinations(members,N//2):
    left_member = member_list
    right_member = list(set(members) - set(member_list))
    left_score = 0
    right_score = 0
    # print("right_member",right_member)
    # print("left_member", left_member)
    for i in range(N//2):
        for j in range(i+1,N//2):
            left_score += table[left_member[i]][left_member[j]]
            left_score += table[left_member[j]][left_member[i]]
            right_score += table[right_member[i]][right_member[j]]
            right_score += table[right_member[j]][right_member[i]]
    ans = min(ans,abs(right_score-left_score))

print(ans)

