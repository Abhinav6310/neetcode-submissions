class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        mem = {}
        n = len(profit)
        def dfs(i,w):
            if i==n:
                return 0
            if (i,w) in mem:
                return mem[(i,w)]
            if w == capacity:
                return 0
            take = 0
            if w+weight[i] <= capacity:
                take = dfs(i+1,w+weight[i])+ profit[i]
            skip = dfs(i+1,w)
            mem[(i,w)] = max(take,skip)
            return mem[(i,w)]
        return dfs(0,0)