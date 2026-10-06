class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)-1
        if n<1:
            return 0
        val = [nums[0]]
        i=0
        ans = 1
        
        while i<=n:
            
            max_step = i + nums[i]
            if max_step>=n:
                return ans
            i_ = i
            for j in range(i,i+nums[i]+1):
                if j>=n:
                    return ans
                if j+nums[j]>i_:
                    i_ = j+nums[j]
                    i = j
            ans = ans+1
        return ans
