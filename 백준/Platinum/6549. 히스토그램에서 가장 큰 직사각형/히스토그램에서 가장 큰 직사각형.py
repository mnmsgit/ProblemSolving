import sys

input = sys.stdin.readline


def largest_rectangle_area(heights):
    # 스택: (start_index, height) 형태로 저장
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        # 현재 막대가 이전 막대보다 낮아지는 경우,
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            width = i - idx  # (오른쪽-왼쪽)
            # 면적 갱신
            max_area = max(max_area, width * height)
            start = idx
        # 스택에 push
        stack.append((start, h))

    length = len(heights)
    while stack:
        idx, height = stack.pop()
        width = length - idx  # 오른쪽 끝은 전체 길이 n
        max_area = max(max_area, width * height)

    return max_area




while True:
    line = list(map(int,input().split()))
    if line[0] == 0:
        break
    n, histogram = line[0], line[1:]
    print(largest_rectangle_area(histogram))




