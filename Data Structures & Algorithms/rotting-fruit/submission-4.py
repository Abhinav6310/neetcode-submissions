class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rotten = deque()
        n = len(grid)
        m = len(grid[0])
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 1:
                    fresh+=1
                elif grid[i][j] ==2:
                    rotten.append((i,j))
        if len(rotten)==0:
            if fresh == 0:
                return 0
            return -1
        visited = set()
        ans = -1
        while len(rotten)>0:
            for i in range(0,len(rotten)):
                ind1 = rotten.popleft()
                for j in range(-1,2):
                    for k in range(-1,2):
                        if abs(j) + abs(k) == 1:
                            dj,dk = ind1[0]+j , ind1[1]+k
                            if min(dj,dk)>=0 and dj<n and dk<m and (dj,dk) not in visited and grid[dj][dk]==1:
                                rotten.append((dj,dk))
                                visited.add((dj,dk))
                                fresh = fresh-1
            ans = ans+1
        if fresh!=0:
            return -1
        return ans
