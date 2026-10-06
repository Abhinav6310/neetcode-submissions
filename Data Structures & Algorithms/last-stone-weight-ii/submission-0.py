class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2
        mem = {}

        def dfs(i, curr):
            if curr > target:
                return float('-inf')

            if curr == target:
                return curr
                
            if i == len(stones):
                return curr

            if (i, curr) in mem:
                return mem[(i, curr)]

            take = dfs(i + 1, curr + stones[i])
            skip = dfs(i + 1, curr)

            mem[(i, curr)] = max(take, skip)
            return mem[(i, curr)]

        val = dfs(0, 0)
        return total - 2 * val