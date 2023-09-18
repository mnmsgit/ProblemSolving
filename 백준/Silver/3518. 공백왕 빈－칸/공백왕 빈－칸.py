
blank = [0] * 180
lines = []

while True:
    try:
        line = input().split()
        lines.append(line)
        i = 0
        for token in line:
            blank[i] = max(blank[i],len(token))
            i += 1
    except:
        break

for line in lines:
    i = 0
    li = []
    for token in line:
        li.append(token)
        for _ in range(blank[i] - len(token)):
            li.append(" ")
        li.append(" ")
        i += 1
    s = "".join(li)
    print(s.rstrip())

