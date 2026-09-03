# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        q = deque([root])
        rst=[]
        lst_2=[]
        while q:

            for i in range(len(q)):
                X=q.popleft()
                if X.left:
                    q.append(X.left)
                if X.right:
                    q.append(X.right)
                lst_2.append(X.val)
            rst.append(lst_2)
            lst_2=[]

            
        return rst