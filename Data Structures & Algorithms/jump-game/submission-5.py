class Solution:
    def canJump(self, nums: List[int]) -> bool:
        right=len(nums)-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=right:
                right = i
            #print(right)
        if right==0:
            return True
        return False