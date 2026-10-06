class Solution:
    def productExceptSelf(self, arr: List[int]) -> List[int]:
        ans = [1]
        for i in range(1,len(arr)):
            ans.append(ans[len(ans)-1]*arr[i-1]) 
        right = arr[len(arr)-1]
        for i in range(len(arr)-2,-1,-1):
            ans[i] = right * ans[i]
            right = right * arr[i]
        
        return ans
