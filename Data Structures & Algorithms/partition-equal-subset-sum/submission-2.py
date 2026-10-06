class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_ = sum(nums)
        if sum_%2!=0:
            return False
        target = sum_//2
        mem = {}
        def dfs(i,rem):
            if rem==0:
                return True
            if i==len(nums):
                return False
            if (i,rem) in mem:
                return mem[(i,rem)]
            take = dfs(i+1,rem-nums[i])
            skip = dfs(i+1,rem)
            mem[(i,rem)] = take or skip
            return mem[(i,rem)]
        return dfs(0,target)