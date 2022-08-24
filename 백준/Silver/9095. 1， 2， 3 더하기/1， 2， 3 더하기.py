import sys

T = int(sys.stdin.readline())
fac = [0for _ in range(11)]
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
