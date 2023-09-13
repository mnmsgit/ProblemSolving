import sys

N = int(sys.stdin.readline())


def same_string(s,left,right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True



def palindrome(s):
    left = 0
    right = len(s)-1
    ans = 0
    if s == s[::-1]:
        return 0
    while left < right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            if same_string(s,left+1,right) or same_string(s,left,right-1):
                return 1
            else:
                return 2
    return 1


for _ in range(N):
    print(palindrome(sys.stdin.readline().strip()))
