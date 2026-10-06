import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(s.split()).lower()
     
        new_s = re.sub(r"[^a-zA-Z0-9]","",ss)
        print(new_s)
        l = 0
        r = len(new_s)-1
        while r > l:
            if new_s[r] == new_s[l]:
                r=r-1
                l=l+1
            else:
                return False
        return True