"""
문자열 문제 풀이
경우 3가지
1. < 가 나온 경우 : 해당 index 직전까지 slicing, tag임 을 명시
2. > 가 나온 경우 : 해당 index 까지 slicing, tag 가 끝남을 명시
3. " "(공백)이 나온 경우 : tag가 아닌 상태라면 해당 index 직전까지 slicing후 문자열 뒤집고 공백 넣어 추가

[::-1] 로 쉽게 문자열 reverse 가능 
"""
# 개행 문자 입역 문제로 strip 사용
import sys

line = sys.stdin.readline().strip()
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
        is_tag = True
    if line[i] == ">":
        sub_str = line[before:i+1]
        output += sub_str
        start = i+1
        is_tag = False
    elif line[i] == " ":
        if not is_tag:
            sub_str = line[before:i]
            sub_str = sub_str[::-1]
            output += sub_str + " "
            start = i+1
    elif i == len(line)-1:
        sub_str = line[before:i+1]
        sub_str = sub_str[::-1]
        output += sub_str

print(output)
