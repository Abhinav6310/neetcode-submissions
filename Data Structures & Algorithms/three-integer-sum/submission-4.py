class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def two_sum(nums):
            l = 1
            r = len(nums)-1
            ans = []
            val = nums[0]
            while r>l:
                if nums[l] + nums[r] + val==0:
                    ans.append([val,nums[l],nums[r]])
                    r = r-1
                    l = l+1
                    while r>l and nums[l]==nums[l-1]:
                        l = l+1
                    while r>l and nums[r]==nums[r+1]:
                        r = r-1
                elif nums[l] + nums[r] + val>0 :
                    r = r-1
                elif nums[l] + nums[r] + val<0:
                    l = l+1
            # print(ans,"****")
            return ans
   
        nums = sorted(nums)
        ans = []
        for i in range(0,len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            ans = ans + two_sum(nums[i:])
        return ans