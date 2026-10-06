class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(ind,i,j,val,visited):
            if val==word:
                return True
            if min(i,j)<0 or i>=len(board) or j>=len(board[0]) or len(val)>=len(word) or (i,j) in visited or word[ind]!=board[i][j]:
                #print(visited)
                return
            visited.add((i,j))
            val = val + board[i][j]
            #print(val)

            if bt(ind+1,i+1,j,val,visited) or bt(ind+1,i-1,j,val,visited) or bt(ind+1,i,j+1,val,visited) or bt(ind+1,i,j-1,val,visited):
                return True
            visited.remove((i, j))

        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if word[0]==board[i][j]:
                    ans = bt(0,i,j,"",set())
                    if ans:
                        return True
        return False