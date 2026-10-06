class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = {}
        def dp(i,j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i>=len(text1) or j>=len(text2):
                return 0
            if text1[i]==text2[j]:
                mem[(i,j)] = 1+dp(i+1,j+1)
            else:
                mem[(i,j)] = max(dp(i+1,j),dp(i,j+1))
            return mem[(i,j)]
        return dp(0,0)