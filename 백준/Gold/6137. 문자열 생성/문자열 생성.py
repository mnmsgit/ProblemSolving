from collections import deque
import sys

def popone(s):
    if s[0] < s[-1]:
        return s.popleft()
    elif s[0] > s[-1]:
        return s.pop()
    else:
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] < s[right]:
                return s.popleft()
            elif s[left] > s[right]:
                return s.pop()
            else:
                left += 1
                right -= 1
        return s.pop()


N = int(sys.stdin.readline())
S = deque()
T = []
for i in range(N):
    S.append(sys.stdin.readline().strip())

while S:
    T.append(popone(S))


loop_count = N//80

for i in range(loop_count):
    print("".join(T[i*80:(i+1)*80]))
print("".join(T[loop_count*80:]))
