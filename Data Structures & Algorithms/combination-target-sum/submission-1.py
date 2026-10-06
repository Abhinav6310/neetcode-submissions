class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #nums = sorted(nums)
        ans = []
        def bt(i,vals,total):
            if total>target or i>=len(nums):
                return
            if total == target:
                ans.append(vals.copy())
                return
            vals.append(nums[i])
            bt(i,vals,total+nums[i])
            vals.pop()
            bt(i+1,vals,total)
        bt(0,[],0)
        return ans