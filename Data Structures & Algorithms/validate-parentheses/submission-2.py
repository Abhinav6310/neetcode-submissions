class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in s:
            if i in ["{","[","("]:
                stk.append(i)
            else:
                if len(stk)==0:
                    return False
                if i=="}" and stk[-1]=="{":
                    stk.pop()
                elif i=="]" and stk[-1]=="[":
                    stk.pop()
                elif i==")" and stk[-1]=="(":
                    stk.pop()
                else:
                    return False
        if len(stk)==0:
            return True
        return False
                
                    