class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:        
        sub_sum = sum(arr[0:k])
        val = k * threshold
        if sub_sum>=val:
            ans = 1
        else:
            ans = 0
        for i in range(1,len(arr)-k+1):
            sub_sum = sub_sum - arr[i-1] + arr[i+k-1]
            if sub_sum>=val:
                ans = ans+1
        return ans