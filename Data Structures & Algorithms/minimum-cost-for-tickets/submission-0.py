class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        mem = {}
        n = len(days)

        def dfs(i):
            if i >= n:
                return 0

            if i in mem:
                return mem[i]

            # 1-day pass
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            take1 = costs[0] + dfs(j)

            # 7-day pass
            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            take7 = costs[1] + dfs(j)

            # 30-day pass
            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            take30 = costs[2] + dfs(j)

            mem[i] = min(take1, take7, take30)
            return mem[i]

        return dfs(0)