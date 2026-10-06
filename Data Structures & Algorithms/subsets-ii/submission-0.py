class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        def sub(i,arr):
            if i==len(nums):
                ans.append(arr.copy())
                return
            if i>len(nums):
                return
            arr.append(nums[i])
            
            sub(i+1,arr)
            arr.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i=i+1
            sub(i+1,arr)
        sub(0,[])
        return ans
