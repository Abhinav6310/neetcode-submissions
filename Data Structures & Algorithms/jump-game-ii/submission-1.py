class Solution:
    def jump(self, nums: List[int]) -> int:
        farthest = 0
        l, r = 0, 0
        ans = 0
        while  r<len(nums)-1:
            #r = nums[l]+l
            for i in range(l,r+1):
                farthest = max(farthest,i+nums[i])
            ans+=1
            l = r+1
            r = farthest
            
            
        return ans

            
                