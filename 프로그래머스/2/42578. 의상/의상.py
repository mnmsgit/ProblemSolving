from collections import defaultdict
def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(int)
    for name, case in clothes:
        clothes_dict[case] +=1
    for key in clothes_dict:
        answer = answer * (clothes_dict[key] + 1)
    answer -= 1
    return answer