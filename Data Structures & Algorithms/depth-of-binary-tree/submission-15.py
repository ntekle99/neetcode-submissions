# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        q = deque()
        q.append(root)
        level = 0
        while q:
            for i in range(len(q)):
                element = q.popleft()
                if element.left:
                    q.append(element.left)
                if element.right:
                    q.append(element.right)
            level+=1
        return level
        
