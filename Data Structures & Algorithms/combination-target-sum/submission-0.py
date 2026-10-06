class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def comb(i,vals,total):
            if total==target:
                ans.append(vals.copy())
                return
            if total>target or i>=len(nums):
                return
            vals.append(nums[i])
            comb(i,vals,total+nums[i])
            vals.pop()
            comb(i+1,vals,total)
        comb(0,[],0)
        return ans
            
            