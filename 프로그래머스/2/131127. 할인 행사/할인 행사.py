def counting(arr):
    flag = True
    for element in arr:
        if element > 0:
            flag = False
    if flag:
        return 1
    return 0
    
def solution(want, number, discount):
    left = 0
    right = 10
    ans = 0
    mart = {}
    for i,element in enumerate(want):
        mart[element] = i
    
    for i in range(10):
        if discount[i] in mart:
            number[mart[discount[i]]] -= 1
    ans += counting(number)
    
    for i in range(len(discount)-10):
        if discount[left] in mart:
            number[mart[discount[left]]] +=1
        if discount[right] in mart:
            number[mart[discount[right]]] -=1
        ans += counting(number)
        left += 1
        right += 1
    
    
    return ans
        
        
        
    