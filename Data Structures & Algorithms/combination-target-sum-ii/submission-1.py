class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        ans = []
        def comb(i,arr,total):
            if total==target:
                ans.append(arr.copy())
                return
            if total>target or i>=len(nums):
                return
            
            arr.append(nums[i])
            comb(i+1,arr,total+nums[i])
            arr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i=i+1
            comb(i+1,arr,total)
        comb(0,[],0)
        return ans

            

