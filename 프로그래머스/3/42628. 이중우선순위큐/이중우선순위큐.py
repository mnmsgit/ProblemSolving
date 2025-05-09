from collections import defaultdict
import heapq
def solution(operations):
    mapping_table = defaultdict(int)
    min_heap = []
    max_heap = []
    for operation in operations:
        operator = operation.split()[0]
        num = int(operation.split()[1])
        if operator == 'I':
            mapping_table[num] +=1
            heapq.heappush(min_heap,num)
            heapq.heappush(max_heap,-num)
        else:
            if num == -1:
                #최솟값 삭제
                while min_heap:
                    delete_element = heapq.heappop(min_heap)
                    if mapping_table[delete_element]:
                        mapping_table[delete_element] -=1
                        break
                
            elif num == 1:
                while max_heap:
                    delete_element = heapq.heappop(max_heap)
                    delete_element = -delete_element
                    if mapping_table[delete_element]:
                        mapping_table[delete_element] -=1
                        break
    arr = []
    for key in mapping_table:
        if mapping_table[key] !=0:
            arr.append(key)
    arr.sort()
    answer = []
    if not arr:
        answer = [0,0]
    else:
        answer = [arr[-1],arr[0]]
        
    return answer