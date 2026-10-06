class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        mem = {}
        def dfs(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if obstacleGrid[i][j]==1:
                return 0
            if i==0 and j==0:
                return 1
            if min(i,j)<0:
                return 0
            
            mem[(i,j)] = dfs(i-1,j) + dfs(i,j-1)
            return mem[(i,j)]
        return dfs(len(obstacleGrid)-1,len(obstacleGrid[0])-1)

        
            