"""
s를 첫째 수를 가장 크게 하는데 먼저 사용
"""
import sys

n = int(sys.stdin.readline())
nums = list(map(int, input().split()))
s = int(sys.stdin.readline())
nums_sorted = sorted(nums, reverse=True)


def s_sort(count, arr):
    ans = []
    i = 0
    j = 0
    k = len(arr)
    while count and j < k:
        index = arr.index(nums_sorted[i])
        if index <= count:
            ans.append(nums_sorted[i])
            arr.pop(index)
            nums_sorted.pop(i)
            count -= index
            i = 0
            j += 1
        else:
            i += 1
    ans.extend(arr)
    return ans


print(*s_sort(s, nums))
