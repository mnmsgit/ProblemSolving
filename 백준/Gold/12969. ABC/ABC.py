import sys

# 0,1,2 로 mapping
letter = ['A', 'B', 'C']

n, k = map(int, sys.stdin.readline().split())
memo = {}


# 조건 만족 개수 계산 로직
def count_condition(arr: list) -> int:
    # 누적합 이용
    length = len(arr)
    subset_sum = [[0,0,0] for _ in range(length+1)]
    count = 0
    for i in range(1,length+1):
        now = arr[i-1]
        if now == 1:
            count += subset_sum[i - 1][0]
        elif now == 2:
            count += subset_sum[i - 1][0]
            count += subset_sum[i - 1][1]
        subset_sum[i] = subset_sum[i-1]
        subset_sum[i][now] += 1
    return count


# N=30임을 고려하여 backtracking 구현(3^^30 + 가지치기)


def backtrack(arr: list, remain_k: int, counts: list) -> list:
    length = len(arr)

    # 길이가 n이면, 남은 k=0일 때만 성공
    if length == n:
        if remain_k == 0:
            return arr
        else:
            return []

    # 메모 체크
    key = (length, remain_k, counts[0], counts[1], counts[2])
    if key in memo:
        return memo[key]
    # A 추가
    arr.append(0)
    counts[0] += 1
    result = backtrack(arr, remain_k, counts)
    if len(result) == n:  # 성공
        memo[key] = result
        return result

    # 실패 시 되돌리기
    arr.pop()
    counts[0] -= 1

    # B 추가
    need = counts[0]  # 지금까지 'A' 개수만큼 쌍 생성
    if remain_k >= need:
        arr.append(1)
        counts[1] += 1
        result = backtrack(arr, remain_k - need, counts)
        if len(result) == n:
            memo[key] = result
            return result
        arr.pop()
        counts[1] -= 1

    # C 추가
    need = counts[0] + counts[1]  # 'A'+ 'B' 개수만큼 쌍 생성
    if remain_k >= need:
        arr.append(2)
        counts[2] += 1
        result = backtrack(arr, remain_k - need, counts)
        if len(result) == n:
            memo[key] = result
            return result
        arr.pop()
        counts[2] -= 1

    # 세 가지 모두 안 되면 실패
    memo[key] = []
    return []


answer_arr = backtrack([], k, [0, 0, 0])
if not answer_arr:        # 못 찾은 경우
    print(-1)
else:
    # 알파벳으로 mapping
    print(''.join(letter[x] for x in answer_arr))