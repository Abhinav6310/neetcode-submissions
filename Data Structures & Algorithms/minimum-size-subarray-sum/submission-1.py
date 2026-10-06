
import numpy as np
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        l = 0
        r = 0
        val = nums[0]
        while r<len(nums):
            if val>=target:
                ans = min(r-l+1,ans)
                val = val-nums[l]
                l = l+1
                if r<l:
                    r=l
            else:
                r= r+1
                if r<len(nums): 
                    val = val + nums[r]
        if ans == float("inf"):
            return 0
        return ans
            