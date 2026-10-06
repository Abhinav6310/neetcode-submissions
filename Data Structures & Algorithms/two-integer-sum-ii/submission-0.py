class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        left = 0
        right = len(arr)-1
        while right > left:
            if arr[left]+arr[right]==target:
                return [left+1,right+1]
            elif arr[left]+arr[right] > target:
                right = right-1
            else:
                left = left+1
        return -1
