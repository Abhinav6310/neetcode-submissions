class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        self.ans = False
        self.ans = False
        used = [False] * len(s1)

        def permute(path):
            if self.ans:  # early exit if already found
                return
            if len(path) == len(s1):  # full permutation formed
                if path in s2:
                    self.ans = True
                return
            
            for i in range(len(s1)):
                if not used[i]:
                    used[i] = True
                    permute(path + s1[i])
                    used[i] = False
        
        permute("")
        return self.ans


        # def checkInclusion(self, s1: str, s2: str) -> bool:
        # self.ans = False
        # used = [False] * len(s1)

        # def permute(path):
        #     if self.ans:  # early exit if already found
        #         return
        #     if len(path) == len(s1):  # full permutation formed
        #         if path in s2:
        #             self.ans = True
        #         return
            
        #     for i in range(len(s1)):
        #         if not used[i]:
        #             used[i] = True
        #             permute(path + s1[i])
        #             used[i] = False
        
        # permute("")
        # return self.ans
                