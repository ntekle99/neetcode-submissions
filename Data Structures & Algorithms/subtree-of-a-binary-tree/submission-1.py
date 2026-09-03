# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(root,subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            elif root.val != subRoot.val:
                return False
            
            leftval = isSameTree(root.left,subRoot.left)
            rightval = isSameTree(root.right,subRoot.right)
            return leftval and rightval
        
        print(subRoot.val)
        bfs = deque()
        bfs.append(root)
        while bfs:
            element = bfs.popleft()
            if element.left:
                bfs.append(element.left)
            if element.right:
                bfs.append(element.right)
            if isSameTree(element,subRoot):
                return True

        return False
            
