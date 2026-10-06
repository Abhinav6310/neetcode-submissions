class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        def dfs(row,col,depth):
            if min(row,col)<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            #visited.add((row,col))
            grid[row][col]= 0
            a = dfs(row+1,col,depth)
            b = dfs(row-1,col,depth)
            c = dfs(row,col+1,depth)
            d = dfs(row,col-1,depth)
            return a+b+c+d+1

        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]==1:
                    area = dfs(i,j,0)
                    ans = max(area,ans)
        return ans