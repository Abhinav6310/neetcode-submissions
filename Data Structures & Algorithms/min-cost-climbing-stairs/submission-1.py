class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)<3:
            return min(cost)
        dp = [-1]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-1],dp[i-2])
            dp[i] = dp[i]+cost[i]
        #print(dp)
        return min(dp[len(cost)-1],dp[len(cost)-2])