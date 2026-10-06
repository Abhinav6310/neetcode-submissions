# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        que = [root]
        ans = []
        while len(que)>0:
            last = len(que)-1
            for i in range(0,len(que)):
                node = que.pop(0)
                if node.left !=None:
                    que.append(node.left)
                if node.right !=None:
                    que.append(node.right)
                if i==last:
                    ans.append(node.val)
        return ans
