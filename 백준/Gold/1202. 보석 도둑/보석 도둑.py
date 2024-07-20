import sys
import heapq


"""
첫 시도
1. 가치순 정렬
2. k 개 가방 중 크기가 item 의 크기 보다 큰 가방 중 가장 작은 가방 선택
1 -> sort
2 -> binary_search 사용 -> 이미 선택된 배낭인 경우 선택된 배낭보다 큰 배낭을 다시 봐야하므로 O(log(N))이 아닌 O(N)이 되는 문제로 시간초과


def b_search(arr,value):
    left = 0
    right = len(arr)-1
    idx = -1
    if len(arr)==1:
        if arr[0] >= value:
            return 0
        else:
            return -1
    while left < right:
        mid = (left + right)//2
        # mid가 작으면 무조건 큰거 봐야
        if arr[mid] < value:
            left = mid +1
        # mid 가 크거나 같으면 작은건 봐야
        else:
            idx = mid
            right = mid
    return idx



N, K = map(int,sys.stdin.readline().split())

jewel = []
bag = []
ans = 0
for _ in range(N):
    M, V = map(int,sys.stdin.readline().split())
    jewel.append((M,V))
for _ in range(K):
    bag.append(int(sys.stdin.readline()))


jewel.sort(key=lambda x:x[1],reverse=True)
bag.sort()
insertable = [True for _ in range(K)]

for i in range(N):
    min_idx = b_search(bag,jewel[i][0])
    if min_idx !=-1:
        for j in range(min_idx,K):
            if insertable[j]:
                insertable[j]= False
                ans += jewel[i][1]
                break
print(ans)
"""

"""
두 번째 시도
1. 가치순 정렬
2. k 개 가방 중 크기가 item 의 크기 보다 큰 가방 중 가장 작은 가방 선택

1 -> sort
2 -> 각 가방이 넣을 수 있는 우선순위 큐
"""


N, K = map(int, sys.stdin.readline().split())
items = []
bags = []
for i in range(N):
    M_i, V_i = map(int, sys.stdin.readline().split())
    items.append((M_i, V_i)) #(무게,가치)


items.sort()
for _ in range(K):
    bags.append(int(sys.stdin.readline()))
bags.sort()
available_items = []
ans = 0
for bag in bags:
    while items:
        if bag >= items[0][0]:
            weight, value = heapq.heappop(items)
            heapq.heappush(available_items, (-value, weight))
        else:
            break

    # bag용량의 맞는 아이템이 있는 경우
    if available_items:
        ans -= heapq.heappop(available_items)[0]
    # 가방에 넣을 수 있는 아이템이 없는 경우 -> 1. item을 모두 담은 경우 종료, 2. 아니면 다음 가방에 대해 판단 진행
    else:
        if not items:
            break
print(ans)
