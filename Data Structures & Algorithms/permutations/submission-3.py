class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        def bt(i,val):
            if i==n:
                self.ans.append(val.copy())
                return
            for j in nums:
                if j not in val:
                    val.append(j)
                    bt(i+1,val)
                    val.pop()
                
        bt(0,[])
        return self.ans
            