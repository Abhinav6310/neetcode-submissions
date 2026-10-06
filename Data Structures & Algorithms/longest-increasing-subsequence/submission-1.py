class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = {}
        n = len(nums)

        def dfs(i):
            if i in mem:
                return mem[i]

            ans = 1  # include nums[i]

            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    ans = max(ans, 1 + dfs(j))

            mem[i] = ans
            return ans

        return max(dfs(i) for i in range(n))