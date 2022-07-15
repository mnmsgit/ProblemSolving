"""
사전상의 배열은 가장 앞의 숫자가 클수록 항상 더 크기 때문에 그리디 알고리즘을 이용해 풀 수 있는 sort 문제이다.
오름차수 배열과 원래의 배열에서 정답인 부분을 pop하고 새로운 배열에 정답인 부분을 append 하여 구했으며 마지막에는 원래의 배열에 남은 값들을 extend하여 종료함.

"""
import sys

n = int(sys.stdin.readline())
nums = list(map(int, input().split()))
s = int(sys.stdin.readline())


def s_sort(count, arr):
    arr_sorted = sorted(arr, reverse=True)
    ans = []
    i = 0  # i는 0 ~ k-j 사이의 값으로 범위 조건이 없어도 while조건 사이에서는 항상 존재하므로 index out range 에러가 생기지 않는다.
    j = 0  # j는 sort가 완료된 갯수
    k = len(arr)  # sort가 완료된 j는 총 배열의 개수인 k보다 작아야한다.
    while count and j < k:
        index = arr.index(arr_sorted[i])
        if index <= count:
            ans.append(arr_sorted[i])
            arr.pop(index)
            arr_sorted.pop(i)
            count -= index
            i = 0
            j += 1
        else:
            i += 1
    ans.extend(arr)
    return ans


print(*s_sort(s, nums))

