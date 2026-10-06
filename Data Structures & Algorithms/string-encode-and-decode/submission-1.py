class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i))+"_"+ str(i)
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        ans = []
        i = 0
        while i<len(s):
            leng = ""
            while True:
                if s[i] != "_":
                    leng = leng+s[i]
                else:
                    break
                i = i+1
            leng = int(leng)
            st = i+1
            end = i+leng+1
            ans.append(s[st:end])
            i = i+leng+1
        
        return ans