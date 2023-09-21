ans =0
def backtracking(arr,idx,numbers,target):
    global ans
    if idx == len(numbers):
        if sum(arr)== target:
            ans+=1
        return
    arr.append(numbers[idx])
    backtracking(arr,idx+1,numbers,target)
    arr.pop()
    arr.append(-numbers[idx])
    backtracking(arr,idx+1,numbers,target)
    arr.pop()
        
def solution(numbers, target):
    backtracking([],0,numbers, target)
    
    return ans