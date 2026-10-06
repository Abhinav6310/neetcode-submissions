class Solution:
    def climbStairs(self, n: int) -> int:
        if n<3:
            return n
        prev_1 = 2
        prev_2 = 1
        ans = 0
        for i in range(3,n+1):
            ans = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = ans
            

        return ans
