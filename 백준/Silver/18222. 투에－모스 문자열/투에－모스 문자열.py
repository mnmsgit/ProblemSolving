# 1번 풀이: 정석적으로 재귀를 이용해 품
# n분할이 아닌 K의 수를 줄이는 방식으로 진행
# 0번이 k가 1일때임을 주의
import sys
K = int(sys.stdin.readline())


def d_c(order, count):
    if not order:
        return count
    expo = len(format(order, 'b'))
    x = order - 2**(expo-1)
    return d_c(x, count+1)


print(d_c(K-1, 0) % 2)


# 2번 풀이: 처음 생각한 풀이 2진수에서 0와 1이 flip 할 때 count 를 늘림
# 즉 2진수에서 1의 개수를 세고 2로나눈 나머지

import sys
K = int(sys.stdin.readline())
print(format(K-1, 'b').count('1') % 2)

