import sys

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

stack = [A[0]]


def b_s(arr, element):
    low = 0
    high = len(arr)-1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < element:
            low = mid + 1
        else:
            high = mid
    return high


for a_i in A:
    if stack[-1] < a_i:
        stack.append(a_i)
    else:
        pos = b_s(stack, a_i)
        stack[pos] = a_i

print(len(stack))
