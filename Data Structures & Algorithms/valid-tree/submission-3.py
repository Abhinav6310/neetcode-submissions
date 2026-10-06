import collections
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges)!=n-1:
            return False
        gph = collections.defaultdict(list)
        for i,j in edges:
            gph[i].append(j)
            gph[j].append(i)
        visited = set()
        def dfs(val,prev):
            # print(val)
            visited.add(val)
            # print(val)
            for i in gph[val]:
                if i==prev:
                    continue
                if i in visited:
                    return False
                if not dfs(i,val):
                    return False
                
            return True
        # print(visited)
        
        ans =  dfs(0,-1)
        if len(visited)!=n:
            return False
        return ans
            

        