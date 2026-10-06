class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_longest(s1,s2):
            ans = ""
            val = min(len(s1),len(s2))
            for i in range(0,val):
                if s1[i] == s2[i]:
                    ans = ans+s1[i]
                else:
                    break
            return ans
        pre = strs[0]
        for i in strs[1:]:
            pre = get_longest(pre,i)
        return pre