class MinHeap:
    
    def __init__(self):
        self.heap = []

    def push(self, val: int) -> None:
        self.heap.append(val)
        ind = len(self.heap)-1
        while True:
            if ind==0:
                break
            parent_ind = (ind-1)//2
            if self.heap[ind]< self.heap[parent_ind]:
               self.heap[ind],self.heap[parent_ind] = self.heap[parent_ind],self.heap[ind] 
               ind = parent_ind
            else:
                break
        return
 
    def pop(self) -> int:
        if len(self.heap)==0:
            return -1
        elif len(self.heap)==1:
            return self.heap.pop()
        else:
            self.heap[0] , self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]
            val = self.heap.pop()
            ind = 0
            while True:
                if (2*ind)+1 <= len(self.heap)-1:
                    if (2*ind)+2 <= len(self.heap)-1:
                        if self.heap[(2*ind)+1] < self.heap[(2*ind)+2]:
                            if self.heap[ind]<self.heap[(2*ind)+1]:
                                break
                            self.heap[(2*ind)+1],self.heap[ind] = self.heap[ind],self.heap[(2*ind)+1]
                            ind = (2*ind)+1
                        else:
                            if self.heap[ind]<self.heap[(2*ind)+2]:
                                break
                            self.heap[(2*ind)+2],self.heap[ind] = self.heap[ind],self.heap[(2*ind)+2]
                            ind = (2*ind)+2
                    else:
                        if self.heap[ind]<self.heap[(2*ind)+1]:
                                break
                        self.heap[(2*ind)+1],self.heap[ind] = self.heap[ind],self.heap[(2*ind)+1]
                        ind = (2*ind)+1
                        break
                else:
                    break
            return val
        
        

    def top(self) -> int:
        if len(self.heap)>0:
            return self.heap[0]
        return -1

    def heapify(self, nums: List[int]) -> None:
        for i in nums:
            self.push(i)
        return
        