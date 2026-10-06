class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = {}
        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if (i,j) in mem:
                return mem[(i,j)]
            if i==0 and j==0:
                return 1
            mem[(i,j)] = dfs(i-1,j) + dfs(i,j-1)
            return mem[(i,j)]
        return dfs(m-1,n-1) 
            