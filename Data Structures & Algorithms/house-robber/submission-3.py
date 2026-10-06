class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i,mem):
            if i>=len(nums):
                return 0
            if i in mem.keys():
                return mem[i]
            mem[i] =  max( nums[i]+dfs(i+2,mem),dfs(i+1,mem) )
            return mem[i]
        return dfs(0,{})
