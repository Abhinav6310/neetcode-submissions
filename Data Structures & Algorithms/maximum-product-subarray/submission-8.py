class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_max = nums[0]
        prev_min= nums[0]
        ans = nums[0]
        for i in nums[1:]:
            if i<0:
                prev_max,prev_min = prev_min,prev_max
            prev_max = max(i , prev_max*i)
            prev_min = min(i , prev_min*i)
            ans = max(prev_max,ans)
        return ans