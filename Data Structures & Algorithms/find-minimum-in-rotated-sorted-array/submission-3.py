class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary_Search(nums,left,right):
            if left==right:
                return left
            mid = left+(right-left)//2
            if nums[mid] > nums[right]:
                return binary_Search(nums,mid+1,right)
            else:
                return binary_Search(nums,left,mid)
        return nums[binary_Search(nums,0,len(nums)-1)]
        