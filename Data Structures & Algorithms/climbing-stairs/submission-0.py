class Solution:
    def climbStairs(self, n: int) -> int:
        self.ans = 0
        def climb(total):
            if total==n:
                self.ans = self.ans +1
                return
            if total>n:
                return
            climb(total+1)
            climb(total+2)
        climb(0)
        return self.ans