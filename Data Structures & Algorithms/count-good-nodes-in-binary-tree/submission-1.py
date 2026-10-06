# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root==None:
            return 0
        self.good = 1

        def count(root, max_val):
            if root==None:
                return
            if root.val >= max_val:
                self.good = self.good+1
                max_val = root.val
            count(root.left,max_val)
            count(root.right,max_val)
        count(root.left,root.val)
        count(root.right,root.val)
        return self.good
