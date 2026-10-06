class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #visited = set()
        ans = 0
        def dfs(row,col):
            if min(row,col)<0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            #visited.add((row,col))
            grid[row][col]= "0"
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j]=="1":
                    dfs(i,j)
                    ans+=1
        return ans
        

            