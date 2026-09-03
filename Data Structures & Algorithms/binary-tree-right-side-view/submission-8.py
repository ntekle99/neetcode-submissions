# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        stk = deque()
        if root is None:
            return []
        self.res = [root.val]
        stk.append(root)
        while stk:
            level = len(stk)
            for i in range(level):
                element = stk.popleft()
                if element.left:
                    stk.append(element.left)
                if element.right:
                    stk.append(element.right)
            if len(stk) !=0:
                self.res.append(stk[-1].val)
        return self.res
