class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(0,len(s)):
            left, right = i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                left = left-1
                right = right+1
                ans+=1
            left, right = i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                left = left-1
                right = right+1
                ans+=1
        return ans

