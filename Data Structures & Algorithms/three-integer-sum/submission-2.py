class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def two_sum(i,left,right):
            ans = []
            find = -nums[i]
            while right>left:
                if nums[left] + nums[right]>find:
                    right = right-1
                elif nums[left] + nums[right]<find:
                    left = left+1
                else:
                    ans.append([nums[i],nums[left],nums[right]])
                    left = left+1
                    right = right-1
                    while right>left and nums[left]==nums[left-1]:
                        left = left+1
                    while right>left and nums[right]==nums[right+1]:
                        right = right-1
            return ans
            
                    

        nums=sorted(nums)
        ans = []
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            val = two_sum(i,i+1,len(nums)-1)
            if len(val)>0:
                for k in val:
                    ans.append(k)

        return ans

