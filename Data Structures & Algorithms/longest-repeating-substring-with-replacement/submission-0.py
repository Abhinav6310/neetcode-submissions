import collections
class Solution:
    def characterReplacement(self, arr: str, k: int) -> int:
        ans = 0
        l=0
        r=0
        while r<len(arr):
            cou = collections.Counter(arr[l:r+1])
            print(cou)
            if (r-l+1) - cou[max(cou,key=cou.get)] <= k :
                if r-l+1>ans:
                    ans = r-l+1
                r = r+1
            else:
                l = l+1
        return ans
            

