class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        ans = s[0]
        for i in range(0,len(s)):
            left, right = i,i
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left>len(ans)-1:
                    ans = s[left:right+1]
                left = left-1
                right = right+1
            left, right = i,i+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                if right-left>len(ans)-1:
                    ans = s[left:right+1]
                left = left-1
                right = right+1
        return ans