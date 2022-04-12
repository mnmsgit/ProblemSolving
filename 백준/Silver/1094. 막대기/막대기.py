x = int(input())
stick_list = [64, 32, 16, 8, 4, 2, 1]
stick_count = 0
for stick in stick_list:
    if x >= stick:
        x = x - stick
        stick_count += 1
        if x == 0:
            break

print(stick_count)

