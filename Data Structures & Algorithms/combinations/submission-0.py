class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def comb(i,val):
            if i > n:
                if len(val) == k:
                    ans.append(val.copy())
                return
            val.append(i)
            comb(i+1,val)
            val.pop()
            comb(i+1,val)
        comb(1,[])
        return ans
