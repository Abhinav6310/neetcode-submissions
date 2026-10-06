class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        coins.sort(reverse=True)
        def dfs(val):
            if val == 0:
                return 0
            if val<0:
                return float("inf")
            if val in mem:
                return mem[val]
            ans = float("inf")
            for i in coins:
                j  = dfs(val-i)
                ans = min(ans,j+1) 
            mem[val] = ans
            return mem[val]
        
        ans =  dfs(amount)
        if ans == float("inf"):
            return -1
        return ans
