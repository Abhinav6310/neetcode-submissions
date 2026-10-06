class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        prev_sum = nums[0]
        for i in nums[1:]:
            prev_sum = prev_sum + i
            #print(prev_sum)
            if prev_sum<0:
                prev_sum=0
            ans = max(ans,prev_sum)
        if ans==0:
            return max(nums)
        return ans
