import sys


def sum_space(size, dice_arr):
    ans = 0
    if size > 1:
        three, two = 4, (2*size-3)*4
        one = size*size*5 - three*3 - two*2
        ans += (one + two + three) * dice_arr[0]
        ans += (two + three) * dice_arr[1]
        ans += three * dice_arr[2]
    return ans


N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
dice_shown = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
dice.sort(), dice_shown.sort()
if N == 1:
    print(sum(dice[:-1]))
else:
    print(sum_space(N, dice_shown))
