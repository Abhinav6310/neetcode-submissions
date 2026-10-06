class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def bt(val):
            if len(val)==len(nums):
                ans.append(val.copy())
                return
            for i in range(0,len(nums)):
                if nums[i] not in val:
                    val.append(nums[i])
                    bt(val)
                    val.pop()
        bt([])
        return ans
                