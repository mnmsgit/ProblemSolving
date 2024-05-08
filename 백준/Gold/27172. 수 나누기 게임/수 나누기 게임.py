import sys
MAX_CARD_NUM = 1000001

N = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

score = [0] * MAX_CARD_NUM
mark = [0] * MAX_CARD_NUM
for element in arr:
    mark[element] = 1

for my_card in sorted(arr):
    dividend = 2 * my_card
    while dividend < MAX_CARD_NUM:
        if mark[dividend]:
            score[my_card] += 1
            score[dividend] -= 1
        dividend += my_card
for element in arr:
    print(score[element], end=" ")

