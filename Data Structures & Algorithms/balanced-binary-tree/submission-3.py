# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root ==None:
            return True
        self.ans = True
        def dfs(root):
            if self.ans == False:
                return 0
            if root==None:
                return 0
            left_ = dfs(root.left)
            right_ = dfs(root.right)
            if abs(dfs(root.right) - dfs(root.left)) > 1:
                self.ans = False
            return max(left_,right_)+1
        dfs(root)
        if self.ans:
            return True
        return False