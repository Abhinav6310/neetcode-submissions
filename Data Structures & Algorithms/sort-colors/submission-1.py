class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 
        r = len(arr)-1
        i = 0
        while r>=i:
            if arr[i]==0:
                arr[i] , arr[l] = arr[l], arr[i]
                i+=1
                l+=1
            elif arr[i]==2:
                arr[i] , arr[r] = arr[r], arr[i]
                r-=1
            else:
                i+=1
        return arr