class MinStack:

    def __init__(self):
        self.minStack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if len(self.minStack)==0:
            self.min_val = val
            self.minStack = [0]
        else:
            self.minStack.append(val-self.min_val)
            if val<self.min_val:
                self.min_val = val

    def pop(self) -> None:
        val = self.minStack.pop()
        if val < 0:
            self.min_val = self.min_val-val

    def top(self) -> int:
        resp =  self.minStack[-1] 
        if resp>0:
            resp = resp+ self.min_val
        else:
            resp = self.min_val
        return resp

    def getMin(self) -> int:
        min_val = self.min_val
        return min_val
