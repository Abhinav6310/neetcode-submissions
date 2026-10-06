class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        ans = -1
        gas_left = 0
        for i in range(0,len(gas)):
            gas_left = gas_left+gas[i]-cost[i]
            if gas_left>=0 :
                if ans ==-1:
                    ans = i
            else:
                ans = -1
                gas_left = 0
        return ans
            