import sys
def validation(arr):
    gather = ["a","e","i","o","u"]
    gather_set = set(gather)
    gather_count = 1
    consonant = 2
    for element in arr:
        if element in gather_set:
            gather_count -= 1
        else:
            consonant -= 1
    if gather_count <= 0 and consonant <= 0:
        return True
    return False


L, C = map(int,sys.stdin.readline().split())

alph = list(map(str, sys.stdin.readline().split()))
alph.sort()


def backtracking(arr,idx):
    global alph
    global L,C
    if len(arr) == L:
        if validation(arr):
            print(*arr,sep="")
        return
    for i in range(idx,C):
        if len(arr) >0:
            if arr[-1] < alph[i]:
                arr.append(alph[i])
                backtracking(arr, idx + 1)
                arr.pop()
        else:
            arr.append(alph[i])
            backtracking(arr, idx + 1)
            arr.pop()


backtracking([], 0)

