class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem = {}
        n = len(profit)
        def dfs(i,w):
            if i>=n:
                return 0
            if (i,w) in mem:
                return mem[(i,w)]
            # if w==capacity:
            #     return 0
            skip = dfs(i+1,w)
            take = 0
            if weight[i]+w<=capacity:
                take = dfs(i,weight[i]+w)+profit[i]
            mem[(i,w)] = max(take,skip)
            return mem[(i,w)]
        return dfs(0,0)