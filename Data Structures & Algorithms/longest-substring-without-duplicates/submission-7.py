class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        val = set()
        val.add(s[0])
        l = 0
        r = 1
        ans = 1
        while r<len(s):
            if s[r] not in val:
                val.add(s[r])
                ans = max(len(val),ans)
            else:
                while s[r] in val and l<r:
                    val.remove(s[l])
                    l+=1
                val.add(s[r])
            r+=1
            print(val)
        return ans
        