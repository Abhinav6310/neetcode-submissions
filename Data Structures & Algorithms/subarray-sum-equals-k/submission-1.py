class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr = 0
        ans = 0
        pre = {0:1}
        for i in nums:
            curr = curr+i
            if curr-k in pre:
                ans = ans+pre[curr-k]
            pre[curr] = pre.get(curr,0)+1
        return ans
