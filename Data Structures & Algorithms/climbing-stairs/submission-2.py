class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i,mem):
            if i==n:
                return 1
            if i>n:
                return 0
            if i in mem.keys():
                return mem[i]
            mem[i] = dp(i+1,mem) + dp(i+2,mem)
            return mem[i]
        return dp(0,{})