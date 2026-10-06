class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        mem = {}
        def dfs(i,curr):
            if i==n:
                if curr==target:
                    return 1
                return 0
            if (i,curr) in mem:
                return mem[(i,curr)]
            
            
            
            add = dfs(i+1,curr+nums[i])
            sub = dfs(i+1,curr-nums[i])
            mem[(i,curr)] = add+sub
            return mem[(i,curr)]
        return dfs(0,0)

