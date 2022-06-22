"""
factorial의 result값을 적당히 sorting 하여 연산해 나감.
과도하게 sorting할 경우 결과값에 오류가 생길 수 있으며 sorting을 적게 할 경우 overflow 발생함.
적당한 sorting 값은 5자리수를 결과로 필요로 하기 때문에 1000000으로 잡음
+
틀려서 result값을 오버플로우가 나지 않는 최대 자릿수인 12자리로 설정했더니 맞음 하지만 반례가 생각나지는 않아 추후에 더 생각해 볼 문제이다.
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

