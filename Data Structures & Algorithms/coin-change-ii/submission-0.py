class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins,reverse = True)
        n = len(coins)
        mem = {}
        def dfs(i,curr):
            if curr==amount:
                return 1
            if i==n or curr>amount:
                return 0
            if (i,curr) in mem:
                return mem[(i,curr)]
            while i<n-1 and coins[i]==coins[i+1]:
                i = i+1
            take = dfs(i,curr+coins[i])
            skip = dfs(i+1,curr)
            mem[(i,curr)] = take + skip
            return mem[(i,curr)]
        return dfs(0,0)