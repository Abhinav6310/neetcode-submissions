class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = [False]*len(nums)
        def func(arr):
            if len(arr)==len(nums):
                ans.append(arr.copy())
                return
            for j in range(len(nums)):
                if seen[j]:
                    continue
                arr.append(nums[j])
                seen[j]=True
                func(arr)
                arr.pop()
                seen[j]=False

        func([])
        return ans
        
                
