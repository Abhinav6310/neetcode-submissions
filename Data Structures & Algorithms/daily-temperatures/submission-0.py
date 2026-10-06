class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        ind_stk = [len(arr)-1]
        ans = [0]*len(arr)
        for i in range(len(arr)-2,-1,-1):
            if arr[i] < arr[ind_stk[-1]]:
                ans[i] = ind_stk[-1] - i
                ind_stk.append(i)
            else:
                while True:
                    if len(ind_stk)==0:
                        ind_stk.append(i)
                        break
                    if arr[i] < arr[ind_stk[-1]]:
                        ans[i] = ind_stk[-1] - i
                        ind_stk.append(i)
                        break
                    else:
                        ind_stk.pop()
        return ans