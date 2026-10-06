class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        n = len(nums)
        nums = sorted(nums)
        def bt(i,val):
            if i==n:
                self.ans.append(val.copy())
                return
            val.append(nums[i])
            bt(i+1,val)
            val.pop()
            while i<n-1 and nums[i]==nums[i+1]:
                i = i+1
            bt(i+1,val)
        bt(0,[])
        return self.ans