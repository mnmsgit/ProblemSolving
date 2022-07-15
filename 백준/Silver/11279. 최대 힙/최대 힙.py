"""
heapq 모듈에 대한 간단한 이해와 최대 힙(max heap) 개념을 간단히 정리
heapq 모듈은 기본적으로 최소 힙만 가능(가장 낮은 숫자가 root이며 자식노드 > 부모노드)
최대힙을 이용하기 위해선 간단한 트릭 사용: (-숫자,숫자)로 이뤄진 tuple을 heap에 저장한다. 이 때 tuple의 첫 값을 읽으므로 절댓값이 가장 큰 숫자가 가장 작은 숫자로 인식함
최대힙을 읽을 때는 튜플의 두번째 값인 [1]을 읽어서 활용
"""
import heapq
import sys

heap = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num:
        heapq.heappush(heap, (-num, num))
    else:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
