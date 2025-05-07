import sys

input = sys.stdin.readline

G = int(input())

# 키: 제곱수, 벨류:수
sq_dict = {}
for i in range(1,100000):
    sq_dict[i**2] = i

ans = []
for key in sq_dict.keys():
    target = key - G
    if target in sq_dict:
        # print(f"과거{sq_dict[target]} 현재{sq_dict[key]}")
        ans.append(sq_dict[key])

if ans:
    for element in ans:
        print(element)
else:
    print(-1)

