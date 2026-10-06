class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def func(arr):
            if len(arr)==len(nums):
                ans.append(arr.copy())
                return
            for j in range(len(nums)):
                if nums[j] in arr:
                    continue
                arr.append(nums[j])
                func(arr)
                arr.pop()
        func([])
        return ans
        
                
