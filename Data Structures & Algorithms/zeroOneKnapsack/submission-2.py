class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem = {}
        
        def dp(i, weight_till):
            if i >= len(profit):
                return 0
            
            if (i, weight_till) in mem:
                return mem[(i, weight_till)]
            
            # skip
            skip = dp(i+1, weight_till)
            
            # take
            take = -float("inf")
            if weight_till + weight[i] <= capacity:
                take = profit[i] + dp(i+1, weight_till + weight[i])
            
            mem[(i, weight_till)] = max(skip, take)
            return mem[(i, weight_till)]
        
        return dp(0, 0)