class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(nums,target,left,right):
            if left>right:
                return False
            mid = left+(right-left)//2
            if nums[mid]==target:
                return True
            if nums[mid]>target:
                return binarySearch(nums,target,left,mid-1)
            else:
                return binarySearch(nums,target,mid+1,right)
        for i in matrix:
            if binarySearch(i,target,0,len(i)-1):
                return True
        return False
                


    