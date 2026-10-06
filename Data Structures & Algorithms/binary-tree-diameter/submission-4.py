# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = -float("inf")
        def dfs(root):
            if root==None:
                return 0
            left_ = dfs(root.left)
            right_ = dfs(root.right)
            height = max(left_, right_)+1
            self.ans =  max(self.ans,left_+right_+1)
            return height
        dfs(root)
        return self.ans-1