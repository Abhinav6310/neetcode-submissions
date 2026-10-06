class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_Search(nums,target,left,right):
            if left>right:
                return -1
            mid = left+(right-left)//2
            if nums[mid]==target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid] :
                    return binary_Search(nums,target,left,mid-1)
                else:
                    return binary_Search(nums,target,mid+1,right)
            else:
                if nums[mid] < target <= nums[right] :
                    return binary_Search(nums,target,mid+1,right)
                else:
                    return binary_Search(nums,target,left,mid-1)
        return binary_Search(nums,target,0,len(nums)-1)

