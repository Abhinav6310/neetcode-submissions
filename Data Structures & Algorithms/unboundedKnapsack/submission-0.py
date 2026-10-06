class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem = {}
        def dp(i,weight_till):
            if i==len(profit):
                return 0
            if (i,weight_till) in mem:
                return mem[(i,weight_till)]
            if weight_till==capacity:
                return 0
            skip = dp(i+1,weight_till)
            include = -float("inf")
            if weight_till + weight[i] <= capacity:
                include = profit[i] + dp(i,weight_till+weight[i])
            mem[(i,weight_till)] = max(include,skip)
            return mem[(i,weight_till)]
        return dp(0,0)