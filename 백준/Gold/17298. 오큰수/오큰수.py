import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = [-1] * N  # 결과를 저장할 리스트, 초기값은 -1로 설정
stack = []

for i in range(N):
    while stack and arr[i] > arr[stack[-1]]:
        # 현재 원소가 스택의 맨 위에 있는 원소보다 큰 경우
        top = stack.pop()
        ans[top] = arr[i]

    stack.append(i)

print(*ans)
