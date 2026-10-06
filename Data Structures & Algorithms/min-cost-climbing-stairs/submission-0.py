class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #self.ans = 0
        def dfs(i,val):
            if i>=len(cost):
                # if val<self.ans:
                #     self.ans = val
                return val
            a = dfs(i+1,val+cost[i])
            b = dfs(i+2,val+cost[i])
            return min(a,b)
        return min(dfs(0,0),dfs(1,0))