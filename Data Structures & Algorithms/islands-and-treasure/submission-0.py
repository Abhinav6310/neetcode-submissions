class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        inf = 2147483647
        n = len(grid)
        m = len(grid[0])
        treasure = deque()
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j]==0:
                    treasure.append((i,j))
        if len(treasure)==0:
            return grid
        cost = 1
        while len(treasure)>0:
            for i in range(0,len(treasure)):
                ind = treasure.popleft()
                for j in directions:
                    dx = ind[0] + j[0]
                    dy = ind[1] + j[1]
                    if min(dx,dy)>=0 and dx<n and dy<m and grid[dx][dy]==inf:
                        treasure.append((dx,dy))
                        grid[dx][dy] = cost
            cost+=1
                
            


        