class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def bt(i,sum_,val):
            if i==len(nums):
                return
            if sum_==target:
                self.ans.append(val.copy())
                return
            if sum_>target:
                return
            val.append(nums[i])
            bt(i,sum_+nums[i],val)
            val.pop()
            bt(i+1,sum_,val)
        bt(0,0,[])
        return self.ans