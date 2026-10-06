import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        ans = right
        while right>=left:
            speed = left + (right-left)//2
            val = 0
            for i in piles:
                val += math.ceil(i/speed)
            if val<=h:
                right = speed-1
                ans = speed
            else:
                left = speed+1
            
        return ans
