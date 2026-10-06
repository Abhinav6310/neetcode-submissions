class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        def bt(i,val):
            if i==len(nums):
                ans.append(val.copy())
                return
            val.append(nums[i])
            bt(i+1,val)
            val.pop()
            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i = i+1
            bt(i+1,val)
        bt(0,[])
        return ans
            