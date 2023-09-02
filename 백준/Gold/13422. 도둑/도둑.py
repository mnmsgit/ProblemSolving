import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N, M, K = map(int,sys.stdin.readline().split())
    houses = list(map(int,sys.stdin.readline().split()))
    houses.extend(houses)
    house_in_a_row = [0] * N
    ans = 0
    house_in_a_row[0] = sum(houses[:M])
    for i in range(1, N):
        house_in_a_row[i] = house_in_a_row[i-1] - houses[i-1] + houses[M+i-1]

    for i in range(N):
        if house_in_a_row[i] < K:
            ans += 1
    if N == M:
        ans = 0 if house_in_a_row[0] >= K else 1
    print(ans)


