class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        ans = 0
        while right>left:
            water = min(height[right],height[left])*(right-left)
            if water>ans:
                ans = water
            if height[right]>height[left]:
                left = left+1
            elif height[left]>height[right]:
                right = right-1
            else:
                left = left+1
                right = right-1
        return ans