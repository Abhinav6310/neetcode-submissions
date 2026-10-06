class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i,mem):
            if i>=len(nums) or i<0:
                return 0
            
            if i+1 not in mem.keys():
                mem[i+1] = dp(i+1,mem)
            if i+2 not in mem.keys():
                mem[i+2] = dp(i+2,mem)
            return max(nums[i]+mem[i+2],mem[i+1])
            
        return dp(0,{})
        #return self.ans
            