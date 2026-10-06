# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        dq = deque([root])
        inner_length = 1
        ans = []
        while len(dq)>0:
            level_ans = []
            level = 0
            while inner_length!=0:
                node = dq.popleft()
                inner_length = inner_length-1
                level_ans.append(node.val)
                if node.left:
                    level = level+1
                    dq.append(node.left)
                if node.right:
                    level = level+1
                    dq.append(node.right)
            inner_length = level
            ans.append(level_ans)
        return ans


                
            

