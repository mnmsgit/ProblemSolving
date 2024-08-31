import sys

N = int(sys.stdin.readline())

a = [False, False] + [True] * (N-1)
prime_num = []

for i in range(2, N+1):
    if a[i]:
        prime_num.append(i)
        for j in range(2*i, N+1, i):
            a[j] = False

left = 0
right = 0


if len(prime_num) == 0:
    print(0)
    exit(0)

subset_sum = prime_num[0]
ans = 0


while True:
    if subset_sum <= N:
        if subset_sum == N:
            ans += 1
        if right == len(prime_num)-1:
            break
        right += 1
        subset_sum += prime_num[right]
    else:
        subset_sum -= prime_num[left]
        left += 1
        if left > right:
            break

print(ans)
