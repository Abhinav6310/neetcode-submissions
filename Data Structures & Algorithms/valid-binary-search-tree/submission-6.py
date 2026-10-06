# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ans = True
        last_val = None
        def dfs(root):
            nonlocal ans, last_val
            if root==None:
                return root
            dfs(root.left)
            if last_val is not None and last_val >= root.val:
                ans = False
            last_val = root.val
            dfs(root.right)
        dfs(root)
        return ans
        