n = int(input())
result_memo = [0 for _ in range(n+1)]
result_memo[0] = 1


def function_t(num):
    result = 0
    if num == 0:
        return 1
    if num == 1:
        result_memo[1] = 1
        return 1
    for k in range(num):
        if result_memo[k] == 0 and result_memo[num - 1 - k] == 0:
            result += function_t(k) * function_t(num - 1 - k)
        elif result_memo[k] == 0:
            result += function_t(k)*result_memo[num - 1 - k]
        elif result_memo[num - 1 - k] == 0:
            result += result_memo[k] * function_t(num - 1 - k)
        else:
            result += result_memo[k]*result_memo[num - 1 - k]
    result_memo[num] = result
    return result


print(function_t(n))
