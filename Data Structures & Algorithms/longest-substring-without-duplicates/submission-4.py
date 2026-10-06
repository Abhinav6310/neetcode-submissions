class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
        if len(arr) < 2:
            return len(arr)

        ans = 1
        l = 0
        r = 1
        inn = set([arr[0]])
        while r < len(arr):
            if arr[r] not in inn:
                inn.add(arr[r])
                r += 1
            else:
                while arr[r] in inn:
                    inn.remove(arr[l])
                    l += 1
            ans = max(ans, len(inn))
        return ans


        

                        