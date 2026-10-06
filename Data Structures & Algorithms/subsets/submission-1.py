class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(i,val):
            if i>len(nums):
                return
            if i==len(nums):
                ans.append(val.copy())
                return
            val.append(nums[i])
            bt(i+1,val)
            val.pop()
            bt(i+1,val)
        bt(0,[])
        return ans
        

            