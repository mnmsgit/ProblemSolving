import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
n_list = list(map(int,input().split()))
m = int(input())
m_list = list(map(int,input().split()))


# n_list 배열에 대한 누적합
n_prefix_sum = [0] * (n+1)
for i in range(1,n+1):
    n_prefix_sum[i] = n_prefix_sum[i-1] + n_list[i-1]

# 부 배열 값을 key: 값, value: 해당 값을 가지는 부 배열 개수로 저장
n_dict = {}

for start in range(n+1):
    for end in range(start+1,n+1):
        subset_sum = n_prefix_sum[end] - n_prefix_sum[start]
        if subset_sum in n_dict:
            n_dict[subset_sum] += 1
        else:
            n_dict[subset_sum] = 1


# m_list 배열에 대한 누적합
m_prefix_sum = [0] * (m+1)
for i in range(1,m+1):
    m_prefix_sum[i] = m_prefix_sum[i-1] + m_list[i-1]


# m 배열에 대해서는 저장하지 않고 n_dict으로 접근하여 바로 더하기
ans = 0

for start in range(m+1):
    for end in range(start+1, m+1):
        subset_sum = m_prefix_sum[end] - m_prefix_sum[start]
        target = t - subset_sum
        if target in n_dict:
            ans += n_dict[target]

print(ans)

