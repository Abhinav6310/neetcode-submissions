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
        ans = []
        while len(dq)>0:
            level_ans = []
            inner_length = len(dq)
            while inner_length!=0:
                node = dq.popleft()
                inner_length = inner_length-1
                level_ans.append(node.val)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            ans.append(level_ans)
        return ans


                
            

