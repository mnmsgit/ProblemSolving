import sys
H, W = map(int,sys.stdin.readline().split())

blocks = list(map(int,sys.stdin.readline().split()))

max_height = max(blocks)

left = 0
right = W-1
l_max = 0
r_max =0
ans = 0
l_idx = -1
r_idx = -1
for i in range(W):
    if blocks[i] == max_height:
        l_idx = i
        break
    if l_max < blocks[i]:
        l_max = blocks[i]
    else:
        ans += l_max-blocks[i]

for i in reversed(range(W)):
    if blocks[i] == max_height:
        r_idx = i
        break
    if r_max < blocks[i]:
        r_max = blocks[i]
    else:
        ans += r_max-blocks[i]

for i in range(l_idx,r_idx):
    ans += max_height - blocks[i]

print(ans)