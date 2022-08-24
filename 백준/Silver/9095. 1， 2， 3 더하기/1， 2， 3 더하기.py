"""
문제 자체는 쉬우나 dp로 풀어야한다는 강박 때문에 시간이 오래 걸린 문제
테스트에서 마주칠 경우 알고리즘은 문제를 해결하기 위한 수단으로 사용해야한다. (알고리즘 쓰기 위해 푸는 것이 아니다.)
순열로  풀고 팩토리얼 사용과정에서 dp사용
"""
import sys

T = int(sys.stdin.readline())
fac = [0 for _ in range(11)]
for i in range(11):
    if i < 2:
        fac[i] = 1
    else:
        fac[i] = fac[i-1]* i
for _ in range(T):
    n = int(sys.stdin.readline())
    case = []
    ans = 0
    rest = n
    for i in range(n//3+1):
        three = i
        rest = n - (3*i)
        for j in range(rest//2+1):
            two = j
            one = rest - (2*j)
            case.append([three, two, one])
    for element in case:
        three, two, one = element[0], element[1], element[2]
        ans += fac[one+two+three]//(fac[one]*fac[two]*fac[three])
    print(ans)

