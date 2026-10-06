import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 
        r = max(piles)
        ans = r
        while l<=r:
            mid = l+(r-l)//2
            time = 0
            for i in piles:
                time = time + math.ceil(i/mid)
            if time<=h:
                r = mid-1
                ans = mid
            elif time>h:
                l = mid+1

        return ans