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

        def dfs(node):
            nonlocal ans, last_val
            if not node:
                return
            dfs(node.left)
            if last_val is not None and node.val <= last_val:
                ans = False
            last_val = node.val
            dfs(node.right)

        dfs(root)
        return ans
        