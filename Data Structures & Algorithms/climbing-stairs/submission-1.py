class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(mem,i):
            if i>n:
                return 0
            if i==n:
                return 1
            if i not in mem.keys():
                #return mem[i]
                mem[i] = dp(mem, i+1) + dp(mem, i+2)
            return mem[i]
        return dp({},0)