# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None:
            return False
        def sameTree(root1,root2):
            if root1 == None and root2 == None:
                return True
            if root1 == None or root2 == None:
                return False
            if root1.val!= root2.val:
                return False
            left = sameTree(root1.left,root2.left)
            right = sameTree(root1.right,root2.right)
            return left and right
        mid = sameTree(root,subRoot)
        if mid:
            return True
        left = self.isSubtree(root.left,subRoot)
        if left:
            return True
        right = self.isSubtree(root.right,subRoot)
        if right:
            return True
        return False
        

            
            