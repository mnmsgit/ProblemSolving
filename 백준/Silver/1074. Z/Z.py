import sys
N, r, c = map(int, input().split())


def find_quadrant(n, row, col):
    quadrants = []  # 4등분한 사각형의 몇 사분면에 들어가는지에 따라 밤위(ex 0~15)를 알 수 있음
    order_num = 0
    while n > 0:
        sidesquare = 2 ** (n - 1)  #4 등분 한 사각형의 각 등분(사각형)의 변의 길이
        if row < sidesquare:
            if col < sidesquare:
                quadrants.append(4**(n-1)*0) 
            else:
                col = col - sidesquare
                quadrants.append(4**(n-1)*1)
        else:
            row = row - sidesquare
            if col < sidesquare:
                quadrants.append(4**(n-1)*2)
            else:
                col = col - sidesquare
                quadrants.append(4**(n-1)*3)
        n = n - 1
    for quadrant in quadrants:
        order_num += quadrant
    return order_num


print(find_quadrant(N, r, c))



