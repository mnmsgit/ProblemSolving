"""
수학문제
주사위의 성질(마주보는 면이 정해져 있음)을 이용한 쉬운 공간문제이다.
딱히 사용된 알고리즘적 기법은 없지만 구현도 중요하기에 연습해볼만 문제
"""
import sys


def sum_space(size, dice_arr):
    ans = 0
    space = size * size * 5
    three, two = 4, (2*size-3)*4
    one = space - three*3 - two*2
    a = [one+two+three, two+three, three]
    for i in range(3):
        ans += a[i] * dice_arr[i]
    return ans


N = int(sys.stdin.readline())
dice = list(map(int, sys.stdin.readline().split()))
dice_shown = [min(dice[0], dice[5]), min(dice[1], dice[4]), min(dice[2], dice[3])]
dice.sort(), dice_shown.sort()
if N == 1:
    print(sum(dice[:-1]))
else:
    print(sum_space(N, dice_shown))
