class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        def reverse(nums,l,r):
            while r>l:
                nums[l] , nums[r] = nums[r] , nums[l]
                r-=1
                l+=1
            return nums
        n = len(nums)
        l = 0
        r = n-1
        k = k%n
        if k==0:
            return 
        
        nums = reverse(nums,l,r)
        l = 0
        r= k-1
        print(r)
        nums = reverse(nums,l,r)
        l=k
        r = len(nums)-1
        print(l)
        reverse(nums,l,r)
