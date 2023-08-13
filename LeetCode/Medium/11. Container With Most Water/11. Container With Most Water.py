class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        ans = 0
        while left < right:
            if height[left] < height[right]:
                ans = max(ans,(right-left)* height[left])
                left +=1
            else:
                ans = max(ans, (right-left)* height[right])
                right -=1
        return ans

