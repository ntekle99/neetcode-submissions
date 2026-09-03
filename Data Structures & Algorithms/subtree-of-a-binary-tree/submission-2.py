# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

        def bfs(root,subroot):
            q = deque()
            q.append(root)
            while q:
                element = q.pop()
                if isSameTree(subroot,element):
                    return True
                elif element.left:
                    q.append(element.left)
                elif element.right:
                    q.append(element.right)
        if bfs(root,subRoot):
            return True
        return False


        