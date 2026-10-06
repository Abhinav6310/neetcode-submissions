class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        ans = nums[0]
        cnt = 1
        for i in nums[1:]:
            if i==ans:
                cnt+=1
            else:
                cnt-=1
        if cnt<0:
            ans = i
        return ans
