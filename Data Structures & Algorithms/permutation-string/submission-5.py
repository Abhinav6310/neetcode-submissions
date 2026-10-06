class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        n = len(s1)
        arr1 = [0]*26
        arr2 = [0]*26
        for i in range(0,n):
            arr1[ord(s1[i]) - ord("a")]+=1
            arr2[ord(s2[i]) - ord("a")]+=1
        if arr1 == arr2:
            return True 
        for i in range(n,len(s2)):
            #print(arr2)
            arr2[ord(s2[i-n]) - ord("a")]-=1
            arr2[ord((s2[i])) - ord("a")]+=1
            if arr1 == arr2:
                return True
        return False