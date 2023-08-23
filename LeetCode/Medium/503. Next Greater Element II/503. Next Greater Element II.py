# sol 1
# Using brute-force -> O(N**2)
class Solution(object):
    def nextGreaterElements(self, nums):
        N = len(nums)
        ans =[-1] * N
        for i in range(N):
            node  = nums[i]
            for j in range(N-1):
                next = (i+j+1)%N
                if nums[next] > node:
                    ans[i] = nums[next]
                    break
        return ans

# sol 2
# Using stack -> O(n**2)
# 총 2*N 탐색으로 완료
# 배열의 뒤에서 부터 역순으로 탐색, stack top이 nums[now] 보디 크면 ans 배열의 now index 갱신
# 아닌 경우 stack을 하나씩 pop
# stack이 빌 때 까지 자신보다 큰 원소가 나타나지 않으면 -1 
class Solution(object):
    def nextGreaterElements(self, nums):
        N = len(nums)
        ans =[-1] * N
        stack = []
        for i in range(0,2*N):
            now = (2*N -i -1) %N
            while stack and stack[-1] <= nums[now]:
                stack.pop()
            if stack:
                ans[now] = stack[-1]
            else:
                ans[now] = -1
            stack.append(nums[now])
        return ans
