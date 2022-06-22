"""
factorial의 result값을 적당히 sorting 하여 연산해 나감.
과도하게 sorting할 경우 결과값에 오류가 생길 수 있으며 sorting을 적게 할 경우 overflow 발생함.
적당한 sorting 값은 5자리수를 결과로 필요로 하기 때문에 1000000으로 잡음
"""


N = int(input())
result = 1
for num in range(2, N+1):
    result *= num
    while True:
        if str(result)[-1] == "0":
            result //= 10
        else:
            break
    result %= 10000000000000

print(str(result)[-5:])

