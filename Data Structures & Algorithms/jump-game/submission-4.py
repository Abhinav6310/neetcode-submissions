class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = {}
        n = len(nums)-1
        self.flag = False
        def dfs(i):
            if self.flag:
                return self.flag
            if i==n:
                return True
            if i>n:
                return False
            if i in mem:
                return mem[i]
            val = False
            for j in range(nums[i], 0, -1):
                val = dfs(i+j)
                if val:
                    self.Flag = True
                    break
            mem[i] = val
            return mem[i]
        return dfs(0)