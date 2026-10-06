class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}
        n = len(prices)
        def dfs(i,can_buy):
            if i >= n:
                return 0
            if (i,can_buy) in mem:
                return mem[(i,can_buy)]
            hold = dfs(i+1,can_buy)
            if can_buy:
                mem[(i,can_buy)] = max(dfs(i+1,not can_buy) - prices[i],hold)
            else:
                mem[(i,can_buy)] = max(dfs(i+2,not can_buy) + prices[i],hold)
            return mem[(i,can_buy)]
        return dfs(0,True)