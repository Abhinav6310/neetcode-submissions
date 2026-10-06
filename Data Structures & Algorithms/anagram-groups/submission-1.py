class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        
        for i in strs:
            inn = [0]*26
            for j in i:
                inn[ord(j)-ord("a")] = inn[ord(j)-ord("a")] + 1
            if str(inn) in list(dic.keys()):
                # dic[str(inn)] = 
                dic[str(inn)] = dic[str(inn)] + [i]
            else:
                dic[str(inn)] = [i]
        return list(dic.values())