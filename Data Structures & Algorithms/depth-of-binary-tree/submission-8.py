# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [root]
        appended_stack = []
        counter = 0
        while len(stack) > 0:
            counter+=1
            
            for i in range(len(stack)):
                element = stack.pop()
                if element.right:
                    appended_stack.append(element.right)
                if element.left:
                    appended_stack.append(element.left)
            stack = appended_stack.copy()
            appended_stack = []
        return counter

#
        