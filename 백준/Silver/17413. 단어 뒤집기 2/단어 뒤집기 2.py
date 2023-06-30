import sys

line = sys.stdin.readline().strip()
token = []
output = ""

is_tag = False
start = 0

for i in range(len(line)):
    before = start
    if line[i] == "<":
        if i:
            sub_str = line[before:i]
            start = i
            if not is_tag:
                sub_str = sub_str[::-1]
            output += sub_str
            token.append(sub_str)
        is_tag = True
    if line[i] == ">":
        sub_str = line[before:i+1]
        output += sub_str
        token.append(sub_str)
        start = i+1
        is_tag = False
    elif line[i] == " ":
        if not is_tag:
            sub_str = line[before:i]
            sub_str = sub_str[::-1]
            output += sub_str + " "
            token.append(sub_str)
            start = i+1
    elif i == len(line)-1:
        sub_str = line[before:i+1]
        sub_str = sub_str[::-1]
        output += sub_str

print(output)