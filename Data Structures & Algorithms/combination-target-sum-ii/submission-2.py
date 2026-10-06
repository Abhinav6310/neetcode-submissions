class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(candidates)
        def bt(i,val,sum_):
            if sum_==target:
                self.ans.append(val.copy())
                return

            if sum_>target or i==len(nums):
                return
            
            val.append(nums[i])
            bt(i+1,val,sum_+nums[i])
            val.pop()

            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i = i+1
            bt(i+1,val,sum_)

        bt(0,[],0)
        return self.ans

            

            
            