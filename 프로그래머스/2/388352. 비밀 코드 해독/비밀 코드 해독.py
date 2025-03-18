from itertools import combinations
def find_intersec(a,b):
    a_set = set(a)
    b_set = set(b)
    return len(a_set.intersection(b_set))
    


def solution(n, q, ans):
    answer = 0
    candidate = []
    is_possible = []
    tmp = [i for i in range(1,n+1)]
    for cand in combinations(tmp,5):
        candidate.append(cand)
        is_possible.append(True)
    for i in range(len(q)):
        query = q[i]
        for j in range(len(candidate)):
            if ans[i] != find_intersec(query,candidate[j]):
                is_possible[j] = False
    answer = is_possible.count(True)
        
    
    return answer