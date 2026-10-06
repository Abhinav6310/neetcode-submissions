class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_flat(nums[1:]),self.rob_flat(nums[:-1]))

    def rob_flat(self,nums):
        prev_2 = 0
        prev_1 = 0
        ans = 0
        for i in range(0,len(nums)):
            ans = max(nums[i]+prev_2 , prev_1)
            prev_2 = prev_1
            prev_1 = ans
        return ans