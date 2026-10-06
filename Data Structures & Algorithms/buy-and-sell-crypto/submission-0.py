class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        ans = 0
        min_val = arr[0]
        for i in arr:
            if min_val > i:
                min_val = i
            if i-min_val > ans:
                ans = i-min_val
        return ans