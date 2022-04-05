from collections import deque

N = int(input())

card_list = deque(range(1, N+1))
discard_list = []
while card_list:
    card = card_list.popleft()
    discard_list.append(card)
    if card_list:
        card = card_list.popleft()
        card_list.append(card)
print(*discard_list)
