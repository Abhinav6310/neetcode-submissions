class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        ans = list()
        for i in range(0,len(arr)):
            l = i+1
            r = len(arr)-1
            if i>0:
                if arr[i]==arr[i-1]:
                    continue
            find = -(arr[i])
            while l<r:
                if arr[l] + arr[r] == find:
                    print(i , l ,r)
                    ans.append([arr[i],arr[l],arr[r]])
                    l = l+1
                    if l>0:
                        while arr[l]==arr[l-1] and r>l:
                            l = l+1
                    r = r-1
                    if r<len(arr)-1:
                        while arr[r]==arr[r+1] and r>l:
                            r = r-1
                elif arr[l] + arr[r] > find:
                    r = r-1
                else:
                    l = l+1
                
        return ans

                
            