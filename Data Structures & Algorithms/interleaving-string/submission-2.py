class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)
        if n1 + n2 != n3:
            return False
        mem = {}
        def dfs(i,j):
            if i==n1 and j==n2:
                return True
            if i == n1:
                return s2[j:] == s3[i+j:]
            if j == n2:
                return s1[i:] == s3[i+j:]
            if (i,j) in mem:
                return mem[(i,j)]
            if s3[i+j] == s1[i] and s3[i+j] == s2[j]:
                a = dfs(i+1,j)
                b = dfs(i,j+1)
                mem[(i,j)] = a or b
            elif s3[i+j] == s1[i]:
                mem[(i,j)] = dfs(i+1,j)
            elif s3[i+j] == s2[j]:
                mem[(i,j)] = dfs(i,j+1) 
            else:
                return False
            return mem[(i,j)]
        return dfs(0,0)

            