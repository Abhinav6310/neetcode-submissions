class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        mem = {}
        def dfs(i,j):
            if i == n1 or j==n2:
                return 0
            if (i,j) in mem:
                return mem[i,j]
            equal = 0
            a = 0
            b = 0
            if text1[i] == text2[j]:
                equal = dfs(i+1,j+1)+1
            else:
                a = dfs(i+1,j)
                b = dfs(i,j+1)
            mem[(i,j)] = max(equal,a,b)
            return mem[(i,j)]
        return dfs(0,0)
            
            
            