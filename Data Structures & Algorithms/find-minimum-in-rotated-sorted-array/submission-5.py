class Solution:
    def findMin(self, arr: List[int]) -> int:
        if len(arr)<2:
            return min(arr)
        left = 0
        right = len(arr)-1
        ans = arr[left]
        while right>left:
            mid = left+(right-left)//2
            if arr[right]>arr[mid]:
                right = mid
            else:
                left = mid+1
        return arr[left]