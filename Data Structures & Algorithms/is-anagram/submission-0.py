class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        import collections
        return collections.Counter(s) == collections.Counter(t)
        

