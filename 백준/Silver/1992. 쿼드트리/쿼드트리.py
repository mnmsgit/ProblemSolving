import sys
N = int(sys.stdin.readline())
image = [[] for _ in range(N)]
for i in range(N):
    image[i] = (list(sys.stdin.readline().strip()))
ans = ""


def d_c(x,y,size):
    global ans
    if size == 1:
        return image[x][y]
    flag = image[x][y]
    same = True
    for j in range(size):
        for k in range(size):
            if flag != image[x+j][y+k]:
                same = False
                break
    if same:
        return flag
    else:
        temp = ""
        temp += "("
        temp += d_c(x,y,size//2)
        temp += d_c(x,y+size//2,size//2)
        temp += d_c(x+size//2,y,size//2)
        temp += d_c(x+size//2,y+size//2,size//2)
        temp += ")"
        return temp



ans += d_c(0,0,N)
print(ans)
