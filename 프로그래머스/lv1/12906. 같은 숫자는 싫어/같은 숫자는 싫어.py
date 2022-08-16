def solution(arr):
    answer = []
    for i in range(len(arr)):
        if not answer:
            answer.append(arr[i])
        else:
            if answer[-1] != arr[i]:
                answer.append(arr[i])
    return answer