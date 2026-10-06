class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        cons = 1
        ans = 1
        nums_set = set(nums)
        for i in range(0,len(nums)):
            if nums[i]-1 not in nums_set:
                while True:
                    if cons>ans:
                        ans = cons
                    if nums[i]+cons in nums_set:
                        cons = cons+1
                    else:
                        break
            cons=1
        return ans
                    
            
