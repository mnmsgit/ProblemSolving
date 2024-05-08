import sys
MAX_CARD_NUM = 1000001

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))


mark = [0] * MAX_CARD_NUM


def card_game():
    global MAX_CARD_NUM
    global mark
    global arr
    score = [0] * MAX_CARD_NUM
    for my_card in sorted(arr):
        dividend = 2 * my_card
        while dividend < MAX_CARD_NUM:
            if mark[dividend]:
                score[my_card] += 1
                score[dividend] -= 1
            dividend += my_card
    temp = []
    for card in arr:
        temp.append(score[card])
    print(*temp)


for element in arr:
    mark[element] = 1

card_game()