# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.val = []
        def dfs(root):
            if root==None:
                return root
            dfs(root.left)
            if len(self.val)>0 and self.val[-1] >= root.val:
                self.ans = False
            self.val.append(root.val)
            
            dfs(root.right)
        dfs(root)
        return self.ans
        