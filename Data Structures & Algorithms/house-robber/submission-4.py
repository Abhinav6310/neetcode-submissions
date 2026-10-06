class Solution:
    def rob(self, nums: List[int]) -> int:
        ans = 0
        prev_2 = 0
        prev_1 = 0
        for i in range(0,len(nums)):
            ans = max(nums[i]+prev_2,prev_1)
            prev_2 = prev_1
            prev_1 = ans
            
        return ans
        