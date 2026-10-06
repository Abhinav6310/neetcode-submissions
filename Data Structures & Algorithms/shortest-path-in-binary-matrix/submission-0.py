class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        q = deque()
        q.append((0,0))
        visited = set()
        visited.add((0,0))
        ans = 0
        while len(q)>0:
            for i in range(0,len(q)):
                ind = q.popleft()
                row,col = ind[0],ind[1]
                if row==n-1 and col==n-1:
                    return ans+1
                for j in range(-1,2):
                    for k in range(-1,2):
                        row1 = row+j
                        col1 = col+k
                        if 0<=row1<len(grid) and 0<=col1<len(grid) and (row1,col1) not in visited:
                            if grid[row1][col1]==0:
                                q.append((row1,col1))
                                visited.add((row1,col1))
            ans = ans+1
        return -1




                


