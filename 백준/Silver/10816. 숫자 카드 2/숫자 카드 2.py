import sys

N = int(sys.stdin.readline().strip())
N_arr = list(map(int, sys.stdin.readline().split()))
N_dict = {}
M = int(sys.stdin.readline().strip())
M_arr = list(map(int, sys.stdin.readline().split()))
for element in N_arr:
    if element in N_dict:
        N_dict[element] = N_dict[element]+1
    else:
        N_dict[element] = 1
# nums = []
# for element in N_dict:
#     nums.append((element,N_dict[element]))
# nums.sort()
# ans = ""
# for element in M_arr:
#     low = 0
#     high = len(element)-1
print(' '.join(str(N_dict[element])if element in N_dict else '0' for element in M_arr))
