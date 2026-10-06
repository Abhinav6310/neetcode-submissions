class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins, reverse=True)
        mem={}
        n=len(coins)
        def dfs(i,til):
            if til==amount:
                return 0
            if til>amount:
                return float("inf")
            if (i,til) in mem:
                return mem[(i,til)]
            if i ==n:
                return float("inf")
            
            take = dfs(i,til+coins[i])+1
            skip = dfs(i+1,til)
            mem[(i,til)] = min(take,skip)
            return mem[(i,til)]
        ans =  dfs(0,0)
        if ans == float("inf"):
            return -1
        return ans
