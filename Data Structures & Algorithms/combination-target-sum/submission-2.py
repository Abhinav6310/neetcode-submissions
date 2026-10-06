class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def bt(i,val,total):
            if total==target:
                ans.append(val.copy())
                return
            if total>target or i>=len(nums) :
                return
            val.append(nums[i])
            bt(i,val,total+nums[i])
            val.pop()
            bt(i+1,val,total)
        bt(0,[],0)
        return ans
